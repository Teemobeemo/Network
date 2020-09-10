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

async function handleDisLike(id) {
    console.log(id);
    const response = await fetch(`/api/dislike?id=${id}`)
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


async function handleFollow(id){
    console.log(id)
    const response = await fetch(`/api/follow?to_follow=${id}`)
    const json = await response.json()
    const followers = json.success
    if(followers){
        console.log(followers)
        document.getElementById('followers').innerText=followers
        // document.getElementById('follow').hidden = True
        document.getElementById('follow').style.display= 'none'
        document.getElementById('unfollow').style.display='block'

    }else{
        // We have an errror
        const error = json.error;
        alert(error)
    }
}

async function handleUnFollow(id){
    console.log(id)
    const response = await fetch(`/api/unfollow?to_follow=${id}`)
    const json = await response.json()
    const followers = json.success
    if(followers){
        console.log(followers)
        document.getElementById('followers').innerText=followers
        document.getElementById('unfollow').style.display='none'
        document.getElementById('follow').style.display='block'
    }else{
        // We have an errror
        const error = json.error;
        alert(error)
    }
}
window.onload = () => {
    const cardbodylist = document.getElementsByClassName('card-body')
    console.log(cardbodylist)
    console.log('ready event')
}