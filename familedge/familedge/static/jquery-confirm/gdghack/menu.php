<?php
/**
 * Created by PhpStorm.
 * User: okirim
 * Date: 26/10/2018
 * Time: 01:24
 */

function search(){
    echo"
    <header class=\"header-area\">

    <!-- Top Header Area -->
    <div class=\"top-header\">
        <div class=\"container\">
            <div class=\"row\">
                <div class=\"col-12\">
                    <div class=\"top-header-content d-flex align-items-center justify-content-between\">
                        <!-- Search Form -->
                        <div class=\"search-form\">
                            <form action=\"#\" method=\"get\">
                                <input type=\"search\" name=\"search\" class=\"form-control\" placeholder=\"Search and hit enter...\">
                                <button type=\"submit\"><i class=\"fa fa-search\"></i></button>
                            </form>
                        </div>

                        <!-- Social Button -->
                        <div class=\"top-social-info\">
                            <a href=\"#\"><i class=\"fa fa-facebook\" aria-hidden=\"true\"></i></a>
                            <a href=\"#\"><i class=\"fa fa-twitter\" aria-hidden=\"true\"></i></a>
                            <a href=\"#\"><i class=\"fa fa-instagram\" aria-hidden=\"true\"></i></a>
                            <a href=\"#\"><i class=\"fa fa-pinterest\" aria-hidden=\"true\"></i></a>
                            <a href=\"#\"><i class=\"fa fa-rss\" aria-hidden=\"true\"></i></a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Logo Area -->
    <div class=\"logo-area text-center\">
        <div class=\"container\">
            <div class=\"row\">
                <div class=\"col-12\">
                    <!-- Nav brand -->
                    <a href=\"index.html\" class=\"nav-brand\"><img src=\"img/core-img/logo.png\" alt=\"\"></a>
                </div>
            </div>
        </div>
    </div>

    <!-- Navbar Area -->
    <div class=\"foode-main-menu\">
        <div class=\"classy-nav-container breakpoint-off\">
            <div class=\"container\">
                <!-- Menu -->
                <nav class=\"classy-navbar\" id=\"foodeNav\">

                    <!-- Nav brand -->
                    <a href=\"index.html\" class=\"nav-brand\"><img src=\"img/core-img/logo.png\" alt=\"\"></a>

                    <!-- Navbar Toggler -->
                    <div class=\"classy-navbar-toggler\">
                        <span class=\"navbarToggler\"><span></span><span></span><span></span></span>
                    </div>

                    <!-- Menu -->
                    <div class=\"classy-menu\">

                        <!-- close btn -->
                        <div class=\"classycloseIcon\">
                            <div class=\"cross-wrap\"><span class=\"top\"></span><span class=\"bottom\"></span></div>
                        </div>

                        <!-- Nav Start -->
                        <div class=\"classynav\">
                            <ul>
                                <li><a href=\"index.html\">Home</a></li>
                                <li><a href=\"index.html\">My Family</a></li>
                                <li><a href=\"#\">DISCIPLINES</a>
                                    <div class=\"megamenu\">
                                        <ul class=\"single-mega cn-col-4\">
                                            <li><a href=\"#\">- HISTOIRE</a></li>
                                            <li><a href=\"#\">- LITERATURE</a></li>
                                            <li><a href=\"#\">- PHILOSOPHIE</a></li>
                                            <li><a href=\"#\">- LEGENDE</a></li>
                                            <li><a href=\"#\">- Bread</a></li>
                                            <li><a href=\"#\">- Breakfast</a></li>
                                            <li><a href=\"#\">- Meat</a></li>
                                            <li><a href=\"#\">- Fastfood</a></li>
                                            <li><a href=\"#\">- Salad</a></li>
                                            <li><a href=\"#\">- Soup</a></li>
                                        </ul>
                                        <ul class=\"single-mega cn-col-4\">
                                            <li><a href=\"#\">- SCIENCE</a></li>
                                            <li><a href=\"#\">- MATHEMATIC</a></li>
                                            <li><a href=\"#\">- TECHNOLOGIE</a></li>
                                            <li><a href=\"#\">- MEDECINE</a></li>
                                            <li><a href=\"#\">- Bread</a></li>
                                            <li><a href=\"#\">- Breakfast</a></li>
                                            <li><a href=\"#\">- Meat</a></li>
                                            <li><a href=\"#\">- Fastfood</a></li>
                                            <li><a href=\"#\">- Salad</a></li>
                                            <li><a href=\"#\">- Soup</a></li>
                                        </ul>
                                        <ul class=\"single-mega cn-col-4\">
                                            <li><a href=\"#\">- GEOLOGIE</a></li>
                                            <li><a href=\"#\">- GEOGRAPHIE</a></li>
                                            <li><a href=\"#\">- ARCHEOLOGIE</a></li>
                                            <li><a href=\"#\">- Recipe</a></li>
                                            <li><a href=\"#\">- Bread</a></li>
                                            <li><a href=\"#\">- Breakfast</a></li>
                                            <li><a href=\"#\">- Meat</a></li>
                                            <li><a href=\"#\">- Fastfood</a></li>
                                            <li><a href=\"#\">- Salad</a></li>
                                            <li><a href=\"#\">- Soup</a></li>
                                        </ul>
                                        <ul class=\"single-mega cn-col-4\">
                                            <li><a href=\"#\">- ROMAN</a></li>
                                            <li><a href=\"#\">- CONTE</a></li>
                                            <li><a href=\"#\">- Travel</a></li>
                                            <li><a href=\"#\">- Recipe</a></li>
                                            <li><a href=\"#\">- Bread</a></li>
                                            <li><a href=\"#\">- Breakfast</a></li>
                                            <li><a href=\"#\">- Meat</a></li>
                                            <li><a href=\"#\">- Fastfood</a></li>
                                            <li><a href=\"#\">- Salad</a></li>
                                            <li><a href=\"#\">- Soup</a></li>
                                        </ul>
                                    </div>
                                </li>
                                <li><a href=\"#\">QUIZ</a></li>
                                <li><a href=\"about-us.html\">PROFILE</a></li>
                            </ul>

                        </div>
                        <!-- Nav End -->
                    </div>
                </nav>
            </div>
        </div>
    </div>
</header>
    ";


}


function slider(){
    echo"
    <section class=\"hero-area\">
    <div class=\"hero-post-slides owl-carousel\">

        <!-- Single Hero Post -->
        <div class=\"single-hero-post\">
            <!-- Post Image -->
            <div class=\"slide-img bg-img\" style=\"background-image: url(img/1.jpg);\"></div>
            <!-- Post Content -->
            <div class=\"hero-slides-content\">
                <p>05/05/2018</p>
                <a href=\"#\" class=\"post-title\">
                    <h4>GOOGLE IO 2018</h4>
                </a>
            </div>
        </div>

        <!-- Single Hero Post -->
        <div class=\"single-hero-post\">
            <!-- Post Image -->
            <div class=\"slide-img bg-img\" style=\"background-image: url(img/1951.jpg);\"></div>
            <!-- Post Content -->
            <div class=\"hero-slides-content\">
                <p>EXEMPLE</p>
                <a href=\"#\" class=\"post-title\">
                    <h4>EXEMPLE</h4>
                </a>
            </div>
        </div>

        <!-- Single Hero Post -->
        <div class=\"single-hero-post\">
            <!-- Post Image -->
            <div class=\"slide-img bg-img\" style=\"background-image: url(img/1951.jpg);\"></div>
            <!-- Post Content -->
            <div class=\"hero-slides-content\">
                <p>EXEMPLE</p>
                <a href=\"#\" class=\"post-title\">
                    <h4>EXEMPLE</h4>
                </a>
            </div>
        </div>

        <!-- Single Hero Post -->
        <div class=\"single-hero-post\">
            <!-- Post Image -->
            <div class=\"slide-img bg-img\" style=\"background-image: url(img/1951.jpg);\"></div>
            <!-- Post Content -->
            <div class=\"hero-slides-content\">
                <p>EXEMPLE</p>
                <a href=\"#\" class=\"post-title\">
                    <h4>EXEMPLE</h4>
                </a>
            </div>
        </div>

        <!-- Single Hero Post -->
        <div class=\"single-hero-post\">
            <!-- Post Image -->
            <div class=\"slide-img bg-img\" style=\"background-image: url(img/1951.jpg);\"></div>
            <!-- Post Content -->
            <div class=\"hero-slides-content\">
                <p>EXEMPLE</p>
                <a href=\"#\" class=\"post-title\">
                    <h4>EXEMPLE</h4>
                </a>
            </div>
        </div>

        <!-- Single Hero Post -->
        <div class=\"single-hero-post\">
            <!-- Post Image -->
            <div class=\"slide-img bg-img\" style=\"background-image: url(img/1951.jpg);\"></div>
            <!-- Post Content -->
            <div class=\"hero-slides-content\">
                <p>EXEMPLE</p>
                <a href=\"#\" class=\"post-title\">
                    <h4>EXEMPLE</h4>
                </a>
            </div>
        </div>

        <!-- Single Hero Post -->
        <div class=\"single-hero-post\">
            <!-- Post Image -->
            <div class=\"slide-img bg-img\" style=\"background-image: url(img/1951.jpg);\"></div>
            <!-- Post Content -->
            <div class=\"hero-slides-content\">
                <p>EXEMPLE</p>
                <a href=\"#\" class=\"post-title\">
                    <h4>EXEMPLE</h4>
                </a>
            </div>
        </div>

        <!-- Single Hero Post -->
        <div class=\"single-hero-post\">
            <!-- Post Image -->
            <div class=\"slide-img bg-img\" style=\"background-image: url(img/1951.jpg);\"></div>
            <!-- Post Content -->
            <div class=\"hero-slides-content\">
                <p>EXEMPLE</p>
                <a href=\"#\" class=\"post-title\">
                    <h4>EXEMPLE</h4>
                </a>
            </div>
        </div>

        <!-- Single Hero Post -->
        <div class=\"single-hero-post\">
            <!-- Post Image -->
            <div class=\"slide-img bg-img\" style=\"background-image: url(img/1951.jpg);\"></div>
            <!-- Post Content -->
            <div class=\"hero-slides-content\">
                <p>EXEMPLE</p>
                <a href=\"#\" class=\"post-title\">
                    <h4>EXEMPLE</h4>
                </a>
            </div>
        </div>

        <!-- Single Hero Post -->
        <div class=\"single-hero-post\">
            <!-- Post Image -->
            <div class=\"slide-img bg-img\" style=\"background-image: url(img/1951.jpg);\"></div>
            <!-- Post Content -->
            <div class=\"hero-slides-content\">
                <p>EXEMPLE</p>
                <a href=\"#\" class=\"post-title\">
                    <h4>EXEMPLE</h4>
                </a>
            </div>
        </div>

    </div>
</section>
    ";

}
