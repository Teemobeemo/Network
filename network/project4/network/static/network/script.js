async function handleLike(id) {
    console.log(id);
    const response = await fetch(`/api/like?id=${id}`)
    const json = await response.json();
    const likes = json.likes
    console.log(likes);
    if (likes) {
        document.getElementById(`like-${id}`).innerText = likes;
        updateLikes();
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
        updateLikes();
    } else {
        const error = json.error;
        alert(error);
    }
}


async function handleFollow(id) {
    // Make response to server
    const response = await fetch(`/api/follow?to_follow=${id}`)
    const json = await response.json()

    // Get the followers from the response
    const followers = json.success

        // Check if the followers is present
    if (followers) {
        // Update the text
        document.getElementById('followers').innerText = followers

        // Show the unfollow btn and remove the follow button
        document.getElementById('follow').style.display = 'none'
        document.getElementById('unfollow').style.display = 'block'

    } else {
        // We have an errror
        const error = json.error;
        alert(error)
    }
}


async function handleUnFollow(id) {
    // Make a response to server to ubfollow the user
    const response = await fetch(`/api/unfollow?to_follow=${id}`)
    const json = await response.json()
    
    // Get the followers from the response
    const followers = json.success

    // Check if the followers is present
    if (followers) {
        
        document.getElementById('followers').innerText = followers

        // Show the follow btn and remove the unfollow button
        document.getElementById('unfollow').style.display = 'none'
        document.getElementById('follow').style.display = 'block'

    } else {
        // We have an errror
        const error = json.error;
        alert(error)
    }
}

// Run the updateLike function when the page is loaded fully
window.onload = async () => {
    updateLikes();
}

// Update the post to show the relevant like or dislike button on the post depending on if the user liked it or not
async function updateLikes() {

    // List of all the cards in the current page
    const cardbodylist = document.getElementsByClassName('card-body')

    // Loop through each one of the cards and do stuff
    for (let i = 0; i < cardbodylist.length; i++) {

        // Get the card form the list
        const card = cardbodylist[i]

        // Get references to the dislike and like button
        const dislike_btn = card.lastElementChild
        const like_btn = dislike_btn.previousElementSibling

        // Continue if the elements are not of type SVG
        if (dislike_btn.nodeName.toLowerCase()!=="svg" || like_btn.nodeName.toLowerCase()!=="svg"){
            continue
        }

        // Get id of the post
        const id = card.id

        // Make request to server to see if the user liked the post
        const response = await fetch(`/api/getlike?id=${id}`)
        const json = await response.json()

        const is_liked = json.status // True or false

        // Check if the is_liked is present
        if (is_liked) {

            // Set styles to buttons to make them appear and disappear
            if (is_liked === "True") {
                like_btn.style.display = "none"
                dislike_btn.style.display = "inline-block"
            } else {
                like_btn.style.display = "inline-block"
                dislike_btn.style.display = "none"
            }
        }
        // Display error if there is one!
        else {
            const err = json.error
            alert(err)
        }
    }

}