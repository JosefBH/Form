var formEl = document.forms.BookPackageForm;
var formData = new FormData(formEl);
var name = formData.get("this");
console.log(name);
