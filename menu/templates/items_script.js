const menuElement = document.getElementById("menu");
const row = document.createElement("div");
row.className = "row";
$('#cleanCart').on('click',()=> localStorage.setItem("sale",JSON.stringify({items:[]})) )
if (localStorage.getItem("sale") === null) {
  localStorage.setItem("sale",JSON.stringify({items:[]}) );
}

items.forEach((item) => {
  const col = document.createElement("div");
  col.className = "col-sm";

  const card = document.createElement("div");
  card.className = "card";
  card.style = "width: 16rem; margin-top:10px;";

  const image = document.createElement("img");
  image.alt = `${item.id} ${item.name}`;
  image.className = "card-img-top";
  image.src = item.photo;

  const cardContent = document.createElement("div");
  cardContent.className = "card-body";

  const name = document.createElement("h2");
  name.append(item.name);
  name.id = "name";
  name.tagName = "name";
  name.className = "card-title";

  const description = document.createElement("p");
  description.append(item.description);
  description.className = "card-text";

  const price = document.createElement("p");
  price.append(`R$${item.price}`);

  const quantityLabel = document.createElement("label");
  quantityLabel.append("Quantidade");

  const quantityInput = document.createElement("input");
  quantityInput.type = "number";
  quantityInput.value=1
  quantityInput.min=1
  quantityInput.className = "form-control form-control-sm";

  const chartButton = document.createElement("button");
  chartButton.append("adicionar");
  chartButton.className = "btn btn-primary";
  chartButton.dataset.toogle = "modal";
  chartButton.dataset.target = "#confirm-modal";
  chartButton.onclick = () => { 
    const local_sale = JSON.parse(localStorage.getItem("sale"));
    const item_sale = { quantity: parseInt(quantityInput.value), ...item };
    let sale_data = { items: [item_sale, ...local_sale.items] };
    localStorage.setItem("sale", JSON.stringify(sale_data));
  };

  cardContent.append(name);
  cardContent.append(description);
  cardContent.append(quantityLabel);
  cardContent.append(quantityInput);
  cardContent.append(price);
  cardContent.append(chartButton);

  card.append(image);
  card.append(cardContent);
  col.append(card);
  row.appendChild(col);
});

menuElement.append(row);
