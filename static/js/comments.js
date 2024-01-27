const editButtons = document.getElementsByClassName("btn-edit"); // all buttons used for edit
const deleteButtons = document.getElementsByClassName("btn-delete"); // all buttons used for delete
const deleteConfirmButton = document.getElementById("deleteConfirm");  // textarea
const commentText = document.getElementById("id_body");  // textarea
const commentForm = document.getElementById("commentForm"); // form
const submitButton = document.getElementById("submitButton"); // the submit button
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));

// Buttond for edit / when user press edit btn to put that comment in id_boby of the comment form

for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let commentId = e.target.getAttribute("comment_id");
        let commentTextBody = e.target.getAttribute("data-comment_text");
        commentText.value = commentTextBody;
        submitButton.innerText = "Update";
        commentForm.setAttribute("action", `edit_comment/${commentId}`);
    });
}

// Button for delete

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let commentId = e.target.getAttribute("comment_id");
        deleteConfirmButton.href = `delete_comment/${commentId}`;
        deleteModal.show();
    });
}