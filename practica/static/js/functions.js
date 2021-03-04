const message_error = (obj) =>{
    let html = '<ul style="text-aling:left;">';
    if (typeof (obj) === 'object'){
        $.each(obj,(key, value)=>{
            html += '<li>'+key+': '+value+'</li>';
        });
        html += '</ul>'
    }
    else{
        html += '<p>'+obj+'</p>';
    }
    Swal.fire({
        title: 'Error!',
        html: html,
        icon: 'error'
    });
}