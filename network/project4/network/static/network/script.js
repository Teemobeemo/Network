async function handleLike(id) {
    console.log(id);
    const response = await fetch(`/api/like?id=${id}`)
    const json = await response.json();
    const likes = json.likes
    console.log(likes);
    if (likes) {
        document.getElementById(`like-${id}`).innerText = likes;
    } else {
        const error = json.error;
        alert(error);
    }
}

