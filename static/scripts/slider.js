$(document).ready(
	function() {
		$('.btn_next_slide').on('click', function() {
			var currentImg = $('.active');
			var nextImg = currentImg.next();

			if (nextImg.length) {
				currentImg.removeClass('active').css('z-index', -10);
				nextImg.addClass('active').css('z-index', 10);
			}
		});

		$('.btn_prev_slide').on('click', function() {
			var currentImg = $('.active');
			var prevImg = currentImg.prev();

			if (prevImg.length) {
				currentImg.removeClass('active').css('z-index', -10);
				prevImg.addClass('active').css('z-index', 10);
			}
		});
	}
);
