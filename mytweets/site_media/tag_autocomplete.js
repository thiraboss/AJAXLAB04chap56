$(document).ready(function () {
	$("#id_tags").autocomplete(
		'/AJAX/tag/autocomplete/',
		{multiple: true, multipleSeparator: ' '}
	);
}); 