document.addEventListener('DOMContentLoaded', function ()
 {
        const mobileMenu = document.querySelector('#mobile-menu');
        const navMenu = document.querySelector('.nav-menu');

        function toggleMenu()
        {
                mobileMenu.classList.toggle('is-active');
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
                        menuLinks.classList.remove('active');
                }
                else 
                {
                        //expand menu for larger screens
                        menu.classList.add('is-active');
                        menuLinks.classList.add('active');
                }
        });  
});