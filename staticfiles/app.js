document.addEventListener('DOMContentLoaded', function ()
 {
        const menu = document.querySelector('#mobile-menu');
        const menuLinks = document.querySelector('.nav-menu');

        function toggleMenu()
        {
                menu.classList.toggle('is-active');
                menuLinks.classList.toggle('active');
        }