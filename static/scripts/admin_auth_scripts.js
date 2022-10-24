const submitLoginForm = (e) => {
    e.preventDefault()
    const login = document.getElementById("login").value
    const password = document.getElementById("password").value

    let xhr = new XMLHttpRequest();
    let url = "/adminLogin";
    xhr.open("POST", url, true)
    xhr.setRequestHeader("Content-Type", "application/json")

    xhr.onreadystatechange = () => {
        console.log(xhr.responseText)
//        location.href = "adminPanel/"
    }

    xhr.send(JSON.stringify({
        "login": login,
        "password": password
    }))
}

window.onload = () => {
    const form = document.getElementById("loginform");
    form.addEventListener('submit', submitLoginForm)
}