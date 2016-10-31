Guide on work
	TODO -> Profile, Admin(?),View Video, Course View, Upload Modal
	
	explain stuff
	- NOTE - a lot of css is in code with margin with percentage(for better scaling with device)
	- app name = ui
	- stuff in static/ui -
		- css -> handle all/some of css in code
		- font -> keep font(now only SAO font)
		- img -> mock for image
		- owl-carousal -> add-on/plug in for carousal
		- temp -> nothing here(old version of owl-carousal)
	- stuff in templates/includes/ 
		- use for including file (if you want to use <input type="date"> remove this folder
- Explain each page in templates
	- ABOUT CAROUSAL 
		- you can view the carousal configure in the owl-carousal webpage 
		and i use version 2 for more function(with more fuking bug). There
		will be config at the bottom of the script block that config each 
		carousal 
	- ALL PAGES
		- All HTML page is extends from navbar.html and that file will have 
		{% block body %} {% block script %} {% block style %} 	
		
	- navbar and navbarnologin
		- main template, there will be cloudfare stuff here too, the no login
		version will have dropdown modal in Sign In button 
	- browse_course 
		-> browsing page with all course, there will be side-nav with the 
		mock up item in it, you need to implement the category here
		The body consist of carousal and the browse all button below
		(which will be use the one that Nut create). 
		You will need to loop through all element in DB to get it's show here
		Note: that the side-nav is with style overflow:hidden which will not 
		be unscrollable so please make sure that the category is fit in page 
		else be sure to remove that style 
	- create
		-> this will handle course creation, there will not be the thumbnail
		picture upload for now so it might need further discuss in group how 
		how you want it to work(i left it though for further use, you can delete
		it if you want)
	- index 
		-> main page - still need bad ass BG from our beloved GOD :P and also 
		carousal can be config at bottom as always. 
		NOTE : The height is still 350px, you might wanna change it to em for percent
		for better device experience
	- register
		-> register - nuff said kappa
	- template 
		-> was gonna used for only cloudflare but i think i will use the navbar for 
		template instead
	- view_course 
		-> view course page, the upload modal is not fix due to fuking designing issue
		will probably finish by the morning :P 