
$("#btnToggleSaleModal").click(() => {
  $("#saleModal").modal("toggle");
  const saleItems = JSON.parse(localStorage.getItem("sale")).items;
  const total_price = saleItems.reduce(
    (value, { quantity, price }) => value + quantity * price,
    0
  );
  const itemsDescription = saleItems.map(({ name, quantity, price }) => {
    return `Nome: ${name} quantidade: ${quantity} preco: R$ ${price} <br/>`;
  });

  $("#modalSaleBody").html(
    `
  items: <br/> ${itemsDescription}
    preço total = R$${total_price}
    <div>
        <label for="inputTableNumber">Numero da mesa</label>
        <input type='number' id="inputTableNumber" name="inputTableNumber" value=1 min=1 class="form-control form-control-sm"/>
    <div>
    <div>
        <label for="inputCustomerNumber">Numero do Cliente</label>
        <input type='number' id="inputCustomerNumber" name="inputCustomerNumber" value=1 min=1 class="form-control form-control-sm"/>
    <div>
    `.replace("/,/", "")
  );
});

$("#btnFinishSale").click(() => {
  const saleItems = JSON.parse(localStorage.getItem("sale")).items;
  const total_price = saleItems.reduce(
    (value, { quantity, price }) => value + quantity * price,
    0
  );
  table_id = $("#inputTableNumber").val();
  customer = $("#inputCustomerNumber").val()
  // csrftoken is necessary for ajax post method
  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === name + "=") {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
  const csrftoken = getCookie("csrftoken");
  
  $.ajax({
    method: "POST",
    data: {
      data: JSON.stringify({
        customer:customer,
        user_token: localStorage.getItem("token"),
        table_id: table_id,
        total_price: total_price,
        items: saleItems.map((saleItem) => {
          return {
            total_price: saleItem.price * saleItem.quantity,
            ...saleItem,
          };
        }),
      }),
    },
    headers: { "X-CSRFToken": csrftoken },
    url: "/new-sale/",

    success: function (response) {
      $(".alert").alert("teste");
      localStorage.setItem("sale", JSON.stringify({ items: [] }));
    },
    error: function (error_data) {
      console.log("error");
      console.log(error_data);
    },
  });

  $("#saleModal").modal("toggle");
});
$("#btnCloseSaleModal").click(() => $("#saleModal").modal("toggle"));
$('#btnNewClient').click(()=>$('#clientModal').modal('toggle'))
