document.body.addEventListener("htmx:afterSettle", function(detail) {
    const dialog = detail.target.querySelector('dialog[data-onload-showmodal]');
    if (dialog) {
        dialog.showModal();
        dialog.addEventListener("close", () => {
            dialog.remove();
        });
    };
});