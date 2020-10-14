/**
 * Открыть/закрыть каталог товаров
 */

function displayModalCategories() {
	const modalCategories_Elem = document.querySelector('#view_categories');
	const page_Elem = document.querySelector('#view_page');
	
	modalCategories_Elem.classList.toggle('container_modal_display');
	page_Elem.classList.toggle('container_display');
}
