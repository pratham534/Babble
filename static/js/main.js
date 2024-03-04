let chatName = ''
let chatSocket = null
let chatWindowUrl = window.location.href
let chatRoomUuid = Math.random().toString(36).slice(2, 12)

console.log("chatRoomUuid", chatRoomUuid)


var chatElement = document.getElementById('chat');
var chatOpenElement = document.getElementById('chat_welcome');
var chatJoinElement = document.getElementById('chat_join');
var chatIconElement = document.getElementById('chat_icon');
var chatWelcomeElement = document.getElementById('chat_welcome');
var chatRoomElement = document.getElementById('chat_room');
var chatNameElement = document.getElementById('chat_name');
var chatLogElement = document.getElementById('chat_log');
var chatInputElement = document.getElementById('chat_input');
var chatSubmitElement = document.getElementById('chat_submit');


function open_chat() {
    // e.preventDefault();

    // var chatWelcomeElement = document.getElementById('chat_welcome');
    // var chatIconElement = document.getElementById('chat_icon');

    chatWelcomeElement.hidden = !chatWelcomeElement.hidden;

    chatIconElement.hidden = true;

    return false;
}


function open_room(){
    
    // var chatWelcomeElement = document.getElementById('chat_welcome');
    // var chatRoomElement = document.getElementById('chat_room');

    chatRoomElement.hidden = !chatRoomElement.hidden;

    chatWelcomeElement.hidden = true;

    return false;
}