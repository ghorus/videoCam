const videoGrid = document.getElementById("video-grid")
const myVideo = document.createElement("video")
myVideo.muted=true
var socket = io()
var peer = new Peer();
navigator.mediaDevices.getUserMedia({
    video:true,
    audio:true
}).then(stream => {
    addVidStream(myVideo,stream)
    peer.on('call',call=>{
        call.answer(stream)
    })
    socket.on('user connected',id=>{
        console.log(id)
        const call = peer.call(id,stream)
        const vid = document.createElement('video')
        call.on('stream',userVidStream=>{
            addVidStream(vid,userVidStream)
        })
    })
})

peer.on('open', id => {
    socket.emit("user connected", id);
  });

function addVidStream(video,stream){
    video.srcObject = stream
    video.addEventListener('loadedmetadata',()=>{
        video.play()
    })
    videoGrid.append(video)
}