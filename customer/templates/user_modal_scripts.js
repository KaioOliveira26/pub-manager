$('#btnCloseUserModal').click(()=>$('#clientModal').modal('toggle'))
$('#btnCloseUserInformationModal').click(()=>$('#clientInformationModal').modal('toggle'))

$('#btnSaveUser').click(()=>{
    const name = $('#inputCustomerName').val()
    const cpf = $('#inputCustomerCPF').val()
    const phone = $('#inputCustomerPhone').val()
    $.ajax({
        method: "POST",
        data: {'name':name, 'cpf':cpf, 'phone':phone},
        headers: { "X-CSRFToken": csrftoken },
        url: "/customer/",
    
        success: function (response) {
          const costumer = response
          console.log(costumer)
          $('#textCustomerId').text(`Numero do Cliente: ${costumer.id}`)
          $('#textCustomerName').text(`Nome do Cliente: ${costumer.name.replace('[','').replace(']','').replace("'","").replace("'","")}`)
          $('#textCustomerCPF').text(`CPF do Cliente: ${costumer.cpf.replace('[','').replace(']','').replace("'","").replace("'","")}`)
          $('#textCustomerPhone').text(`Telefone do Cliente: ${costumer.phone.replace('[','').replace(']','').replace("'","").replace("'","")}`)

          $('#clientInformationModal').modal('toggle')
          $('#clientModal').modal('toggle')
        },
        error: function (error_data) {
          console.log("error");
          console.log(error_data);
        },
      });
    
})