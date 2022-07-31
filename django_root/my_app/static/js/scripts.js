let lightMode = localStorage.getItem('lightMode');
const lightModeToggle = document.querySelector('#color_theme_toggle');

function saveToggle(){
    var checkbox = document.getElementById('color_theme_toggle');
    localStorage.setItem('color_theme_toggle', checkbox.checked);
}

function enableToggle(){    
    var checked = JSON.parse(localStorage.getItem('color_theme_toggle'));
    document.getElementById("color_theme_toggle").checked = checked;
}

function enableLightMode() {
    document.body.classList.add('light_mode');
    localStorage.setItem('lightMode', 'enabled');
}

const disableLightMode = () => {
    document.body.classList.remove('light_mode');
    localStorage.setItem('lightMode', null);
}

// this keeps the setting the same as it was the last time the client was on the site.
// since lightMode is local storage, the clients computer will remember if it was selected last time.
if (lightMode == "enabled") {
    enableLightMode();
    enableToggle();
}

lightModeToggle.addEventListener('click', () => {
    lightMode = localStorage.getItem('lightMode');
    if (lightMode !== "enabled") {
        enableLightMode();
    } else {
        disableLightMode();
    }
    saveToggle();
});

