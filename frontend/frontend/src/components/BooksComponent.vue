<template>
    <div class="jumbotron-vertical-center">
    <div class="container">
        <!-- bootswatch CDN -->
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/darkly/bootstrap.min.css" integrity="sha384-nNK9n28pDUDDgIiIqZ/MiyO3F4/9vsMtReZK39klb/MtkZI3/LtjSjlmyVPS3KdN" crossorigin="anonymous">

        <div class="row">
            <div class="col-sm-12">
                <p> Book Library 📚 </p>
                <hr><br>
                <button type="button" class="btn btn-success btn-sm">Add Book</button>
                <br><br>
                <table class="table table-hover">
                   <thead>
                    <tr>
                        <th scope="col">Title</th>
                        <th scope="col">Genre</th>
                        <th scope="col">Read?</th>
                        <th scope="col">Actions</th>
                    </tr>
                   </thead>
                   <tbody>
                    <tr>
                        <td>DO</td>
                        <td>RE</td>
                        <td>ME</td>
                        <td>
                            <div class="btn-group" role="group">
                                <button type="button" class="btn btn-danger btn-sm">Add</button>
                                <button type="button" class="btn btn-info btn-sm">Update</button>
                                <button type="button" class="btn btn-danger btn-sm">Delete</button>
                            </div>
                        </td>
                    </tr>
                   </tbody>
                </table>
 
            </div>
        </div>
    </div>
</div>
</template>