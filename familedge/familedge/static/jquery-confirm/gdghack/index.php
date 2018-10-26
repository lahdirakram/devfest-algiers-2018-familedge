<?php
/**
 * Created by PhpStorm.
 * User: okirim
 * Date: 26/10/2018
 * Time: 00:56
 */
require("menu.php");
?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="description" content="">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <!-- The above 4 meta tags *must* come first in the head; any other head content must come *after* these tags -->

    <!-- Title -->
    <title>Foode - Food Blog HTML5 Template</title>

    <!-- Favicon -->
    <link rel="icon" href="img/core-img/favicon.ico">

    <!-- Core Stylesheet -->
    <link rel="stylesheet" href="style.css">

</head>

<body>
<!-- ##### Preloader ##### -->
<div class="preloader d-flex align-items-center justify-content-center">
    <div class="circle-preloader">
        <img src="img/core-img/logo.png" alt="">
        <div class="foode-preloader">
            <span></span>
        </div>
    </div>
</div>

<!-- ##### Header Area Start ##### -->
<?php search(); ?>
<!-- ##### Header Area End ##### -->

<!-- ##### Hero Area Start ##### -->
<?php slider()?>

<!-- ##### Hero Area End ##### -->

<!-- ##### Blog Content Area Start ##### -->
<section class="blog-content-area section-padding-100">
    <div class="container">
        <div class="row">
            <!-- Featured Post Area -->
            <div class="col-12">
                <div class="featured-post-area">
                    <div id="featured-post-slides" class="carousel slide d-flex flex-wrap" data-ride="carousel">

                        <div class="carousel-inner">

                            <div class="carousel-item active bg-img" style="background-image: url(img/2.jpg)">
                                <!-- Featured Post Content -->
                                <div class="featured-post-content">
                                    <p>HISTORY</p>
                                    <a href="#" class="post-title">
                                        <h2>HOW WAS THE WORLD !</h2>
                                    </a>
                                </div>
                            </div>

                        </div>

                        <ol class="carousel-indicators">
                            <li data-target="#featured-post-slides" data-slide-to="0" class="active">
                                <h2>LES VIKINGS</h2>
                                <a href="#" class="post-title">
                                    <nav>jhon marston</nav>
                                </a>
                            </li>
                            <li data-target="#featured-post-slides" data-slide-to="1">
                                <h2>Exemple</h2>
                                <a href="#" class="post-title">
                                    <h5>Exemple</h5>
                                </a>
                            </li>
                            <li data-target="#featured-post-slides" data-slide-to="2">
                                <h2>Exemple</h2>
                                <a href="#" class="post-title">
                                    <h5>Exemple Exemple Exemple</h5>
                                </a>
                            </li>
                            <li data-target="#featured-post-slides" data-slide-to="3">
                                <h2>Exemple</h2>
                                <a href="#" class="post-title">
                                    <h5>Exemple Exemple Exemple</h5>
                                </a>
                            </li>
                            <li data-target="#featured-post-slides" data-slide-to="4">
                                <h2>Exemple</h2>
                                <a href="#" class="post-title">
                                    <h5>Exemple Exemple Exemple</h5>
                                </a>
                            </li>
                        </ol>

                    </div>
                </div>
            </div>
        </div>


<!-- ##### Footer Area Start ##### -->
<footer class="footer-area">
    <div class="container">
        <div class="row">
            <div class="col-12">
                <!-- Footer Social Info -->
                <div class="footer-social-info d-flex align-items-center justify-content-between">
                    <a href="#"><i class="fa fa-facebook"></i><span>Facebook</span></a>
                    <a href="#"><i class="fa fa-twitter"></i><span>Twitter</span></a>
                    <a href="#"><i class="fa fa-google-plus"></i><span>Google +</span></a>
                    <a href="#"><i class="fa fa-linkedin"></i><span>linkedin</span></a>
                    <a href="#"><i class="fa fa-instagram"></i><span>Instagram</span></a>
                    <a href="#"><i class="fa fa-vimeo"></i><span>Vimeo</span></a>
                    <a href="#"><i class="fa fa-youtube"></i><span>Youtube</span></a>
                </div>
            </div>
        </div>

        <div class="row">
            <div class="col-12">
                <div class="copywrite-text">
                    <p><!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. -->
                        Copyright &copy;<script>document.write(new Date().getFullYear());</script> All rights reserved | This template is made with <i class="fa fa-heart-o" aria-hidden="true"></i> by <a href="https://colorlib.com" target="_blank">Colorlib</a>
                        <!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. --></p>
                </div>
            </div>
        </div>
    </div>
</footer>
<!-- ##### Footer Area Start ##### -->

<!-- ##### All Javascript Script ##### -->
<!-- jQuery-2.2.4 js -->
<script src="js/jquery/jquery-2.2.4.min.js"></script>
<!-- Popper js -->
<script src="js/bootstrap/popper.min.js"></script>
<!-- Bootstrap js -->
<script src="js/bootstrap/bootstrap.min.js"></script>
<!-- All Plugins js -->
<script src="js/plugins/plugins.js"></script>
<!-- Active js -->
<script src="js/active.js"></script>
</body>

</html>
