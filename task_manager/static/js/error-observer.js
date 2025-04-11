const errorDecorator = document.getElementById('error-decorator');
    
const observer = new MutationObserver((mutationsList) => {
    for (const mutation of mutationsList) {
        if (mutation.type === 'childList') {
            mutation.addedNodes.forEach((node) => {
                const errorModal = document.getElementById('error-modal');
                if (errorModal) {
                    setTimeout(() => {
                        errorModal.innerHTML = '';
                    }, 5000);
                }
            });
        }
    }
});