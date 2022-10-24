function showLectures() {
    let xhr = new XMLHttpRequest();
    let url = "/adminTools";
    xhr.open("POST", url, true)
    xhr.setRequestHeader("Content-Type", "application/json")
    xhr.send(JSON.stringify({"showLectures": 0}))
}

function addLecture() {
    let xhr = new XMLHttpRequest();
    let url = "/adminTools";
    xhr.open("POST", url, true)
    xhr.setRequestHeader("Content-Type", "application/json")
    xhr.send(JSON.stringify({"addLecture": 0}))
}

function addCourse() {
    let xhr = new XMLHttpRequest();
    let url = "/adminTools";
    xhr.open("POST", url, true)
    xhr.setRequestHeader("Content-Type", "application/json")
    xhr.send(JSON.stringify({"addCourse": 0}))
}

// function changeIndOfCourse() {
//     let xhr = new XMLHttpRequest();
//     let url = "/adminTools";
//     xhr.open("POST", url, true)
//     xhr.send({"changeIndOfCourse": 0})

// }