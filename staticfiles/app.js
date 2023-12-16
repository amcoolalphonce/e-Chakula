document.addEventListener('DOMContentLoaded', function ()
 {
        const mobileMenu = document.querySelector('#mobile-menu');
        const navMenu = document.querySelector('.nav-menu');

        function toggleMenu()
        {
                mobileMenu.classList.toggle('is-active');
                navMenu.classList.toggle('active');
        }

        mobileMenu.addEventListener('click', toggleMenu);
        window.addEventListener('resize', function ()
         {
                const windowWidth = window.innerWidth;

                if (windowWidth<=768)
                {
                        //collapse menu for small screens
                        mobileMenu.classList.remove('is-active');
                        navMenu.classList.remove('active');
                }
                else 
                {
                        //expand menu for larger screens
                        menu.classList.add('is-active');
                        menuLinks.classList.add('active');
                }
        });  
});