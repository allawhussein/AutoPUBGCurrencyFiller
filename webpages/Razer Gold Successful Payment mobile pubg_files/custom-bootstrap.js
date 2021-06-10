$(document).ready(function(){
	/*bootstrap-select*/
	/*
	$('#basic').selectpicker({
		//liveSearch: true,
		maxOptions: 1
	});
	*/
	function redesignDot(){
		var i;
		var lenght = $('.promote ul li').length;
		//console.log(lenght);
		for (i = 0; i < lenght; i++) { 
			$(".promote ul .media.img-icon:nth-child("+ i +")").prepend('<i class="fa fa-circle"></i>');
		} 

	}
	//error-message em - molpay, telsel
	function errMsg(errText) {
		var temp = '<div class="container-err-msg">'
			+ '<div class="align">'	
				+ '<ul class="fa-ul text--sm red-color">';
				
					for (i = 0; i < errText.length; i++) { 
						if (i==0) {
							temp += '<li><span class="fa-li"><i class="rzr-icon-alert-line text--md"></i></span>'+ errText[i] +'</li>'
						} else {
							temp += '<li><span class="fa-li"><i></i></span>'+ errText[i] +'</li>'
						}								
					}
					
				temp +=  '</ul>'
			+ '</div>'
		+ '</div>';	
		
		return temp;
	};
	//animate tick
	function totalSection() {		
		$total = $('.container-info.animate .section-display').length;
		//add all class
		$('.container-info.animate .section-display').addClass("hidden");
	
	}
	function resizeoval() {
		var $_addition_width = 300;
		var $_width = $( window ).width() + $_addition_width;
		var $_height = ( $_width / 10 );
		var $_borderRadius = ($_width / 2) + "px / " + ($_height / 2) + "px" ;
		var $_marginTop = "-54px"; //can not change
		var $_marginLeft = "-" + ($_addition_width / 2) + "px";
		
		$(".oval").css("width", $_width);
		$(".oval").css("height", $_height);
		$(".oval").css("border-radius", $_borderRadius);
		$(".oval").css("margin-top", $_marginTop);
		$(".oval").css("margin-left", $_marginLeft);
		
		if ($_height > 62){
			$(".dynamic-mt").css("margin-top", "-" + ($_height - 62) + "px");
		} 
	}
	function sequenceSection($tempNum) {
		if($tempNum == 0){
			resizeoval();			
		}
		
		//add 1 by 1 of class sequeces
		$('.container-info.animate .section-display').eq($tempNum).removeClass("hidden");
		$('.container-info.animate .section-display').eq($tempNum).addClass("active");										
	}		
	totalSection();		
		
	function drawTick() {
		$(".trigger").toggleClass("drawn")
	}
	
	
	var i = 0;
	var $_sec = 300;
	myVar = setInterval(
		function(){   
			
			if (i == $total) {
				i = 0;	
				clearTimeout(myVar);
				return
			}
			
			sequenceSection(i);
			if (i == 0){
				//need animate the tick path						
			}
			i = i + 1;
			
		},
		
		$_sec  /* 10000 ms = 10 sec */
		
	);
	setTimeout(drawTick, 0);	
	
	
	//top navigation select

	$('.rz-dropdown-country').selectpicker();
	$('.rz-dropdown-lang').selectpicker();
	
	//this will make the web to first
	$(".region-switcher-header").click(function(event){
		$('#regionCollapse.collapse').collapse('toggle');
		event.preventDefault();
	});
	
	$('.rz-checkbox').change(function() {
		if($(this).hasClass("checked")) {
			$(this).removeClass("checked");
			
		}else{
			$(this).addClass("checked");
		}
	});
	
	$('.otp-selected').selectpicker({
		//liveSearch: true,
		maxOptions: 1
	});
	$('.amount-selected').selectpicker({
		//liveSearch: true,
		maxOptions: 1
	});
	
	$('[data-toggle="tooltip"]').tooltip(); 
	/*bootstrap-popover - sample 2*/
	
	//footer mobile view click
	$(".toggle-another").each(function() {
		var targetId = "#".concat($(this).data("toggle")),
		target = $(targetId);
		void 0 != target && $(this).click(function(e) {
			e.preventDefault(), target.toggleClass("open"), $(this).toggleClass("open")
		})
	});
	//payweb dropdown details
	$('.is[data-target="#totalSilver"]').click(function(){
		if ($(".is").hasClass("collapsed")){
			$(".rzr-icon-triangle-down").addClass("rzr-icon-triangle-up");
			$(".rzr-icon-triangle-up").removeClass("rzr-icon-triangle-down");
		} else {
			$(".rzr-icon-triangle-up").addClass("rzr-icon-triangle-down");
			$(".rzr-icon-triangle-down").removeClass("rzr-icon-triangle-up");
		}
	});
								
	/*for shoping cart - dropdown*/
	
	$( ".panel-title" ).click(function() {
		if ($(".game-heading .fa-chevron-up")[0]){
			$(".game-heading .fa.fa-chevron-up").addClass("fa-chevron-down");
			$(".game-heading .fa.fa-chevron-up").removeClass("fa-chevron-up");
			
			$(".panel-body").css("display", "none");
			$(".game-list").css("visibility", "hidden");
			$(".game-heading .fa.fa-shopping-cart").css("visibility", "visible");
			$(".header-amount").css("visibility", "visible");
			
		}else{
			$(".game-heading .fa.fa-chevron-down").addClass("fa-chevron-up");
			$(".game-heading .fa.fa-chevron-down").removeClass("fa-chevron-down");
			
			$(".panel-body").css("display", "block");
			$(".game-list").css("visibility", "visible");
			$(".game-heading .fa.fa-shopping-cart").css("visibility", "hidden");
			$(".header-amount").css("visibility", "hidden");
		}
	});
	/*avoid using repeated existing class name -- sample 'panel-body' will not do */
	$( "#panel-note-term .dropdown" ).click(function() {
		if ($(".note-term .fa-chevron-up")[0]){
			$(".note-term .fa.fa-chevron-up").addClass("fa-chevron-down");
			$(".note-term .fa.fa-chevron-up").removeClass("fa-chevron-up");
			//$(".panel-body").css("display", "none");
			$(".panel-description .description").css("visibility", "hidden");			
			$(".panel-description").css("display", "none");
			
			
		}else{
			$(".note-term .fa.fa-chevron-down").addClass("fa-chevron-up");
			$(".note-term .fa.fa-chevron-down").removeClass("fa-chevron-down");
			
			$(".panel-description .description").css("visibility", "visible");
			$(".panel-description").css("display", "block");
			
		}
	});
	
	
	/*.loadandwait.fadeout.ng-hide*/
	
	$('.loadandwait.fadeout.autoclose').css({opacity: 1.0, visibility: "visible"}).animate({opacity: 0}, 3000);
	setTimeout(hidePopup, 3000);

	
	function hidePopup() {
		$(".loadandwait.fadeout.autoclose").css("display", "none");
	}
	
	/*loading zgold - zsilver coin*/
	
	$('.component-page-loader.autoclose').css({opacity: 1.0, visibility: "visible"}).animate({opacity: 0}, 3000);
	setTimeout(hidePopupLonding, 3000);

	
	function hidePopupLonding() {
		$(".component-page-loader.autoclose").css("display", "none");
	}

	
	
	
	
	
	//custom selected
	//RenderSelect();

   // inspired by http://jsfiddle.net/arunpjohny/564Lxosz/1/
	$('.table-responsive-stack').find("th").each(function (i) {
      
		$('.table-responsive-stack td:nth-child(' + (i + 1) + ')').prepend('<span class="table-responsive-stack-thead">'+ $(this).text() + ':</span> ');
		$('.table-responsive-stack-thead').hide();
	});
   
	$( '.table-responsive-stack' ).each(function() {
		var thCount = $(this).find("th").length; 
		var rowGrow = 100 / thCount + '%';
		//console.log(rowGrow);
		$(this).find("th, td").css('flex-basis', rowGrow);   
	});
   
   
   
   
function flexTable(){
	if ($(window).width() < 500) {
      
		$(".table-responsive-stack").each(function (i) {
			$(this).find(".table-responsive-stack-thead").show();
			$(this).find('thead').hide();
		});
		  
		
	   // window is less than 768px   
	} else {
		  
		  
		$(".table-responsive-stack").each(function (i) {
			$(this).find(".table-responsive-stack-thead").hide();
			$(this).find('thead').show();
		});
   }
// flextable   
}      
 
flexTable();
   
window.onresize = function(event) {
	
    flexTable();
	
	resizeoval();	
	
	
	if ($(".regular.slick-slider")[0]){
		var delayInMilliseconds = 1000; //1 second
		//callAdjustTitleContainer();

		setTimeout(function() {
			//console.log('window resize');
			//need relay for get correct value
			callAdjustTitleContainer();
		}, delayInMilliseconds);
	}
	if ($(".direct-topup.slick-slider")[0]){
		var delayInMilliseconds = 1000; //1 second
		//callAdjustTitleContainer();

		setTimeout(function() {
			//console.log('window resize');
			//need relay for get correct value
			callAdjustTitleContainerDirectTopup();
		}, delayInMilliseconds);
	}
};
   
   
   
		
});
	/*modify to function - otp*/
	
	/*custom select option - otp*/
	function RenderSelect() {
		var x, i, j, selElmnt, a, b, c;
		/*look for any elements with the class "otp-select":*/
		x = document.getElementsByClassName("otp-select-1");
		for (i = 0; i < x.length; i++) {
			selElmnt = x[i].getElementsByTagName("select")[0];
			
			/*for each element, create a new DIV that will act as the selected item:*/
			a = document.createElement("DIV");
			a.setAttribute("class", "select-selected");
			//console.log('95 -' + selElmnt.selectedIndex + ' ' + selElmnt.options[selElmnt.selectedIndex]);
			if (selElmnt.options[selElmnt.selectedIndex] === undefined) {
				//console.log('97 -' + x + ' ' + selElmnt.options[0].innerHTML + ' ');
				a.innerHTML = selElmnt.options[0].innerHTML;
			}else{
				//console.log('100 -' + x );
				a.innerHTML = selElmnt.options[selElmnt.selectedIndex].innerHTML;
			}
			
			x[i].appendChild(a);
			/*for each element, create a new DIV that will contain the option list:*/
			b = document.createElement("DIV");
			b.setAttribute("class", "select-items select-hide");
			for (j = 1; j < selElmnt.length; j++) {
				/*for each option in the original select element,
				create a new DIV that will act as an option item:*/
				c = document.createElement("DIV");
				c.innerHTML = selElmnt.options[j].innerHTML;
				
				c.addEventListener("click", function(e) {
					/*when an item is clicked, update the original select box,
					and the selected item:*/
					var y, i, k, s, h;
					s = this.parentNode.parentNode.getElementsByTagName("select")[0];
					h = this.parentNode.previousSibling;
					
					for (i = 0; i < s.length; i++) {
						console.log('125 -' + h + ' ' + s + ' ' + this.innerHTML);
						if (s.options[i].innerHTML == this.innerHTML) {
							s.selectedIndex = i;
							h.innerHTML = this.innerHTML;
							y = this.parentNode.getElementsByClassName("same-as-selected");
							for (k = 0; k < y.length; k++) {
								y[k].removeAttribute("class");
							}
							this.setAttribute("class", "same-as-selected");
							break;
						}
					}
					console.log(h);
					h.click();
				});
				
				b.appendChild(c);
			}
			x[i].appendChild(b);
			/*when the select box is clicked, close any other select boxes,
				and open/close the current select box:*/
			
			a.addEventListener("click", function(e) {
				/*console.log('150 - test');*/
				e.stopPropagation();
				closeAllSelect(this);
				this.nextSibling.classList.toggle("select-hide");
				this.classList.toggle("select-arrow-active");
				
			});
			
		}
	}
	
	function closeAllSelect(elmnt) {
		/*a function that will close all select boxes in the document,
		except the current select box:*/
		var x, y, i, arrNo = [];
		x = document.getElementsByClassName("select-items");
		y = document.getElementsByClassName("select-selected");
		for (i = 0; i < y.length; i++) {
			if (elmnt == y[i]) {
				arrNo.push(i)
			} else {
				y[i].classList.remove("select-arrow-active");
			}
		}
		for (i = 0; i < x.length; i++) {
			if (arrNo.indexOf(i)) {
				x[i].classList.add("select-hide");
			}
		}
	}
	/*if the user clicks anywhere outside the select box,
	then close all select boxes:*/
	document.addEventListener("click", closeAllSelect);			

	/*only can key in numeric*/
	
	//function numeric(id){
	//$("input.only-numeric").keydown(function (e) {	//has problem first time
	jQuery(document).on('keydown', 'input.only-numeric', function(e) {	
		// Allow: backspace, delete, tab, escape, enter and .
		if ($.inArray(e.keyCode, [46, 8, 9, 27, 13, 110]) !== -1 ||
			 // Allow: Ctrl+A, Command+A
			(e.keyCode === 65 && (e.ctrlKey === true || e.metaKey === true)) || 
			 // Allow: home, end, left, right, down, up
			(e.keyCode >= 35 && e.keyCode <= 40)) {
				 // let it happen, don't do anything
				 return;
		}
		// Ensure that it is a number and stop the keypress
		if ((e.shiftKey || (e.keyCode < 48 || e.keyCode > 57)) && (e.keyCode < 96 || e.keyCode > 105)) {
			e.preventDefault();
		}
	});			
		
	//}	
//for popup message	
	function closeMessage () {	
		$(".messagebox.fadeout").removeClass("fadeout");			
	}
	function openMessage () {	
		$(".messagebox").addClass("fadeout");			
	}

	
	//for cookies and other messagebox
	/*for popup messagebox*/
	/*cy added 20181001*/   
	//this function can remove a array element.
	Array.remove = function(array, from, to) {
		var rest = array.slice((to || from) + 1 || array.length);
		array.length = from < 0 ? array.length + from : from;
		return array.push.apply(array, rest);
	};

	//this variable represents the total number of popups can be displayed according to the viewport width
	var total_popups = 0;
	
	//arrays of popups ids
	var popups = [];

	//this is used to close a popup
	function close_popup(id)
	{
		for(var iii = 0; iii < popups.length; iii++)
		{
		
			if(id == popups[iii])
			{
				Array.remove(popups, iii);
				
				$('#'+ id + '_container').removeClass('slide');
				setTimeout(function(){				
					calculate_popups();
				}, 600);
				return;
			}
		}   
	}

	//displays the popups. Displays based on the maximum number of popups that can be displayed on the current viewport width
	function display_popups()
	{
	
		var bottom = 20;
		
		var iii = 0;
		
		var temp = 0; //for height messagebox
		for(iii; iii < total_popups; iii++)
		{
		
			if(popups[iii] != undefined)
			{
				var element = document.getElementById(popups[iii]+'_container');
				
				//console.log('height -- ' + $('#' + popups[iii]+'_container').css("height"));
				temp = $('#' + popups[iii]+'_container').css("height");
				temp = temp.replace("px", "")
				element.style.bottom = bottom + "px";				
				
				bottom = bottom + parseInt(temp) + 50; /*padding-top =20px, padding-bottom  =20px, between gap =10px */
				element.style.display = "block";
			}
		}
		
		for(var jjj = iii; jjj < popups.length; jjj++)
		{
			var element = document.getElementById(popups[jjj]);
			element.style.display = "none";
		}
		
	}
	
	//creates markup for a new popup. Adds the id to popups array.
	function call_popup(id)
	{
		
		var exist = 0;
		for(var iii = 0; iii < popups.length; iii++)
		{  
		console.log(popups[iii]);
		
			//already registered. Bring it to front.
			if(id + '_popup' == popups[iii])
			{
			
				Array.remove(popups, iii);			
				//popups.unshift(id + '_popup');	
				popups.push(id + '_popup');					
				calculate_popups();			
				exist = 1;
				return;
			}else{
				exist = 0;
			}
		}
		
		$('#' + id +'_popup_container').addClass("slide");
		//popups.unshift(id + '_popup');
		popups.push(id + '_popup');	
		
		calculate_popups();
		
	}
	
	//calculate the total number of popups suitable and then populate the toatal_popups variable.
	function calculate_popups()
	{				
		total_popups = 2; //control can display how many popup 
		display_popups();		
	}
	
	//recalculate when window is loaded and also when window is resized.
	window.addEventListener("resize", calculate_popups);
	window.addEventListener("load", calculate_popups);	
		
		
	
	