document.addEventListener('DOMContentLoaded', function () {

    function switchAuth() {
        const login = document.getElementById('login-view');
        const register = document.getElementById('register-view');
        const isLoginVisible = window.getComputedStyle(login).display !== 'none';
        if (isLoginVisible) {
            login.style.display = 'none';
            register.style.display = 'block';
        } else {
            login.style.display = 'block';
            register.style.display = 'none';
        }
    }
    window.switchAuth = switchAuth;

    function togglePass(id) {
        const input = document.getElementById(id);
        if (!input) return;
        input.type = input.type === 'password' ? 'text' : 'password';
    }
    window.togglePass = togglePass;


    // 1. Detectamos el entorno
    const isGitHubPages = window.location.hostname.includes('github.io');
    
    // 2. Definimos la raíz del proyecto dependiendo de dónde se ejecute
    const rootPath = isGitHubPages
        ? `${window.location.origin}/Hebra-Tech/Pages` // En GitHub Pages (asumiendo que 'Pages' está en la raíz)
        : '.'; // En local, como login.html está al mismo nivel que Admin y Roles, empezamos desde el directorio actual

    // 3. Mapeamos las rutas exactas respetando tu árbol de carpetas
    const roleMap = {
        administrador: `${rootPath}/Admin/Admin.html`,
        operario: `${rootPath}/Roles/Operario.html`,
        cliente: `${rootPath}/Roles/Cliente.html`
    };


    const form = document.getElementById('login-form');
    if (form) {
        form.addEventListener('submit', function (e) {
            e.preventDefault();
            const role = document.getElementById('role-select').value;
            if (!role) { alert('Por favor selecciona un rol.'); return; }
            const target = roleMap[role];
            if (target) { window.location.href = target; }
            else { alert('Rol no válido'); }
        });
    }

});