let commentForm = document.getElementById('comment_form')

commentForm.onsubmit = function(form){
    form.preventDefault();
    let description = document.getElementById('description').value;
    console.log(description)

    const options = {
        method: 'POST',
        body: JSON.stringify({
            'csrfmiddlewaretoke': '{{ csrf_token }}',
            'description':description}),
        headers: {
            'Content-Type': 'application/json'
        }
    }

    fetch('{% url "post-detail" post.slug %}', options)
    .then(response => console.log(response))
}
