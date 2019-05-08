#!/usr/bin/python3.6


import cgi
import os


print("Context-Type:text/html")
print("")





print('''
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="shortcut icon" href="/favicon.ico" type="image/x-icon">
    <link rel="icon" href="/icon1.png" type="image/x-icon">


    <title> CLOUD DEVELOPERS</title>

    <!-- Bootstrap core CSS -->
    <link href="/css/bootstrap.min.css" rel="stylesheet">
		<script src="/js/jquery-3.2.1.min.js"></script>
		<script src="/js/bootstrap.min.js"></script>
    <!-- Custom styles for this template -->
    <!--link href="jumbotron.css" rel="stylesheet"-->
	<style>
		.dropbtn {
			background-color:white:
   			 color: black;
   			 padding: 10px;
   			 font-size: 16px;
   			 border: none;
    		cursor: pointer;
		}
		.dropdown {
			position: absolute;
   			 display: block;
		}
		.dropdown-content {
    		display: none;
    		position: absolute;
		 	min-width: 160px;
			box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
    		z-index: 1;
		}
		.dropdown-content a {
		 	color: black;
		 	padding: 8px 8px;
			text-decoration: none;
    		display: block;
		}
		.dropdown-content a:hover {background-color: #f1f1f1}
		.dropdown:hover .dropdown-content {
    		display: block;
		}
		.dropdown-submenu {
    	position: relative;
		}
		.dropdown-submenu .dropdown-menu {
    	top: 0;
    	left: 100%;
    	margin-top: -1px;
		}
	</style>
<link rel="stylesheet" href="/css/bootstrap.min.css"/>
        <link rel="stylesheet" href="/css/font-awesome.min.css"/>
        <link rel="stylesheet" href="/css/magnific-popup.css"/>
        <link rel="stylesheet" href="/css/owl.carousel.min.css"/>
        <link rel="stylesheet" href="/css/style.css"/>
        <link rel="stylesheet" href="/css/animate.css"/>

  </head>

  <body>

<!-- Header section -->
        <header class="header-section">
                <div class="container">
                        <h4>
                        <a href="/index.html">
                        Cloud Env.
                        </a>
                        </h4>
                        <!-- Switch button -->
                        <div class="nav-switch">
                                <div class="ns-bar"></div>
                        </div>
                        <div class="header-right">
                                <ul class="main-menu">
                                        <li class="active"><a href="index.html" class="site-btn sb-c1">HOME</a></li>
                                        <li><a href="#"class="site-btn sb-c2">Support</a></li>
                                        <li><a href="/index.html" class="site-btn sb-c3">Logout</a></li>
                                </ul>
                        </div>

                </div>
        </header>
        <!-- Header section end -->
<br/><br/><br/><br/><br/>


    <nav class="navbar navbar-inverse navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <a class="navbar-brand" href="#" style="color:#F1F1F6;">CLOUD SERVICES</a>
          <a class="navbar-brand" href="/index.html" style="color:#F1F1F6;">LOGOUT</a>
        </div>
      </div>
    </nav>
    <div class="jumbotron">
      <div class="container">
        <h1 style="color:#5F5F5F;">Hello !!!</h1>
        <p>Welcome to <strong style="color:#5F5F5F;">CLOUD SERVICES</strong> . You are free to choose any of our services listed below and we guarantee you very good perforamnce in exchange of a paltry amount. These cloud services also conatin Amazon Cloud Services. </p>
        <p><a class="btn btn-primary btn-lg" href="#" role="button">Learn more &raquo;</a></p>
      </div>
    </div>

    <div class="container">
      <div class="row">
        <div class="col-md-4">
          <h2 style="color:blue;">IAAS<small> INFRASTRUCTURE AS A SERVICE</small> </h2>
          <p>We provide you with OS such as RedHat and Ubuntu and Windows</p>
          <p><a class="btn btn-default" href="/iaaschoose.html" role="button">View details &raquo;</a></p>
        </div>
        <div class="col-md-4">
          <h2 style="color:blue;">STAAS <small> STORAGE AS A SERVICE</small></h2>
          <p>Thinking of a service that wont let u feel you are running out of space. Here we are at your door with our STAAS service</p>
         <!--<p><a class="btn btn-default" href="/staas.html" role="button">View details &raquo;</a></p>-->
	  <p><font color="green">Coming Soon...!!!</font></p>
       </div>
        <div class="col-md-4">
          <h2 style="color:blue;">PAAS <small> PLATFORM AS A SERVICE</small></h2>
          <p>Enjoy our docker conatiner services for interpreters of languages such as Python, Ruby, Java, Perl...!! </p>
          <!--<p><a class="btn btn-default" href="/cgi-bin/paas/paas.py" role="button">View details &raquo;</a></p>-->
	  <p><font color="green">Coming Soon...!!!</font></p>
        </div>
      </div>
<!--	 <div class="row">
        <div class="col-md-4">
         <img src="images.png">
        </div>
        <div class="col-md-4">
          	<img src="staas1.jpg">	
	</div>

        <div class="col-md-4">
          	<img src="paas.png">	
	</div>-->
	<script>
		$(document).ready(function(){
  		$('.dropdown-submenu a.test').on("click", function(e){
    		$(this).next('ul').toggle();
  			e.stopPropagation();
  			e.preventDefault();
			});
		});
</script>

  </body>
</html>

''')

