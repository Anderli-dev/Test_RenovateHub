/*
┌────────────────────────────────────┐
│         Цей код вкрадений          │
│     Але вкрав його не я, а уточка) │
└────────────────────────────────────┘

        _
Кря! >(.)__
      (___/    
*/
    let draggedEl = null;

    function onDragStart(event) {
        draggedEl = event.currentTarget;
        event.dataTransfer.effectAllowed = "move";
    }
    
    function onDragOver(event) {
        event.preventDefault();
    }
    
    function onDrop(event, projectID) {
        event.preventDefault();
    
        const dropTarget = event.currentTarget;
        if (!draggedEl || draggedEl === dropTarget) return;
    
        const list = document.getElementById(`tasks-list-${projectID}`);
    
        if (draggedEl.compareDocumentPosition(dropTarget) & Node.DOCUMENT_POSITION_FOLLOWING) {
            list.insertBefore(draggedEl, dropTarget.nextSibling);
        } else {
            list.insertBefore(draggedEl, dropTarget);
        }
    
        updateOrder(projectID);
    }
    
    function updateOrder(projectID) {
        const taskItems = document.querySelectorAll(`#tasks-list-${projectID} [data-task-id]`);
        taskItems.forEach((el, index) => {
            const taskId = el.dataset.taskId;
            
            const newOrder = index;
    
            const badge = el.querySelector(".badge");
            if (badge) {
                badge.textContent = "#" + newOrder;
            }
    
            fetch("{% url 'task_reorder' %}", {
                method: "POST",
                headers: {
                    "X-CSRFToken": "{{ csrf_token }}",
                    "Content-Type": "application/x-www-form-urlencoded"
                },
                body: `task_id=${taskId}&new_order=${newOrder}`
            });
        });
    }
    
    function moveTask(buttonEl, direction, projectID) {
        const currentItem = buttonEl.closest("[data-task-id]");
        const list = document.getElementById(`tasks-list-${projectID}`);
    
        if (direction === "up" && currentItem.previousElementSibling) {
            list.insertBefore(currentItem, currentItem.previousElementSibling);
        } else if (direction === "down" && currentItem.nextElementSibling) {
            list.insertBefore(currentItem.nextElementSibling, currentItem);
        }
    
        updateOrder(projectID);
    }