const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();



// jquery: removes error message after 5 seconds
setTimeout(function() {
    $('#message').fadeOut('slow');
}, 5000);
