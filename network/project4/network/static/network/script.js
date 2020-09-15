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

// Run the updateLike and the textArea grow function when the page is loaded fully
window.onload = async () => {
    const textAreas = document.getElementsByClassName('textarea')
    for (let i =0; i<textAreas.length; i++){
        const textArea = textAreas[i];
        textArea.style.height = "5px";
        textArea.style.height = (textArea.scrollHeight)+"px";
        textArea.style.overflow = 'hidden'
    }
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
        const likeBox = card.getElementsByClassName('like-box').item(0)

        // Get references to the dislike and like button
        const dislike_btn = likeBox.lastElementChild
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

// Get the csrf token from the browser
function csrfcookie () {
    var cookieValue = null,
        name = 'csrftoken';
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
};

// Edit post function
async function acceptBtn(id){
    const textarea = document.getElementById(`textarea-${id}`);
    const content = textarea.value;
    
    const response = await fetch('/api/edit/',{
        method: 'POST', 
        headers: {
          'Content-Type': "application/json; charset=UTF-8",
          "X-CSRFToken":csrfcookie(),
        },
        body: JSON.stringify({post:id,post_content:content})
      });
    const json = await response.json()
    const status = json.status

    if(status){
        // Successful
        const textarea = document.getElementById(`textarea-${id}`);
        const editBTN = document.getElementById(`edit-btn-${id}`);
        const acceptBTN = document.getElementById(`accept-${id}`);
        const declineBTN = document.getElementById(`decline-${id}`);
        
        textarea.style.resize='none'
        textarea.readOnly = true;
          editBTN.style.display='inline-block'
        acceptBTN.style.display='none'
        declineBTN.style.display='none'  }
    else{
        alert(json.error)
    }
}

function showEditBtn(id){
    // Get the text area
    const textarea = document.getElementById(`textarea-${id}`);
localStorage.setItem(`text-${id}`,textarea.style.height)
    // If no textarea found
    if (!textarea){
        console.error('No text area found')
        return;
    }

    // Make the text area editable
    textarea.style.resize='vertical'
    textarea.readOnly = false

    const editBTN = document.getElementById(`edit-btn-${id}`);
    const acceptBTN = document.getElementById(`accept-${id}`);
    const declineBTN = document.getElementById(`decline-${id}`);

    editBTN.style.display='none'
    acceptBTN.style.display='inline-block'
    declineBTN.style.display='inline-block'

}


async function declineBtn(id){
    const textarea = document.getElementById(`textarea-${id}`);
    const editBTN = document.getElementById(`edit-btn-${id}`);
    const acceptBTN = document.getElementById(`accept-${id}`);
    const declineBTN = document.getElementById(`decline-${id}`);
    
    textarea.style.resize='none'
    textarea.readOnly = true
    
    textarea.style.height = localStorage.getItem(`text-${id}`);

    editBTN.style.display='inline-block'
    acceptBTN.style.display='none'
    declineBTN.style.display='none'

    // Get the post content
    
    const response = await fetch(`/api/post/content?id=${id}`)
    const json = await response.json()

    const content = json.content
    if(!content){
        alert(error)
        return
    }
    textarea.value = content
}