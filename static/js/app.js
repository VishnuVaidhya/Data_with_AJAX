$.ajax({
    url:  '/students/list',
    type:  'get',
    dataType:  'json',
    success: function  (data) {
        let rows =  '';
        data.studs.forEach(stud => {
        rows += `
        <tr>
            <td>${stud.student_name}</td>
            <td>${stud.enroll_number}</td>
            <td>${stud.student_image.url}</td>
            <td>${stud.gender}</td>
            <td>${stud.city}</td>
            <td>${stud.state}</td>
            <td>${stud.country}</td>
            <td>
                <button class="btn deleteBtn" data-id="${room.id}">Delete</button>
                <button class="btn updateBtn" data-id="${room.id}">Update</button>
            </td>
        </tr>`;
    });
    $('[#myTable](https://paper.dropbox.com/?q=%23myTable) > tbody').append(rows);
    $('.deleteBtn').each((i, elm) => {
        $(elm).on("click",  (e) => {
            deleteRoom($(elm))
        })
    })
    }
});