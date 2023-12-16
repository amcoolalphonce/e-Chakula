document.addEventListener('DOMContentLoaded', function ()
 {
        const menu = document.querySelector('#mobile-menu');
        const menuLinks = document.querySelector('.nav-menu');

        function toggleMenu()
        {
                menu.classList.toggle('is-active');
                menuLinks.classList.toggle('active');
        }

        menu.addEventListener('click', toggleMenu);
        window.addEventListener('resize', function ()
         {
                const windowWidth = window.innerWidth;
                if (windowWidth<=768)
                {
                        //collapse menu for small screens
                        menu.classList.remove('is-active');
                }
        }