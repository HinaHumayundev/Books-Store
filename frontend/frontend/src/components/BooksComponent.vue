<template>
    <div class="jumbotron-vertical-center">
    <div class="container">
        <!-- bootswatch CDN -->
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/slate/bootstrap.min.css" integrity="sha384-8iuq0iaMHpnH2vSyvZMSIqQuUnQA7QM+f6srIdlgBrTSEyd//AWNMyEaSF2yPzNQ" crossorigin="anonymous">
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
                    <tr v-for="book, i in books" :key="i">
                        <td>{{book.title}}</td>
                        <td>{{book.genre}}</td>
                        <td>
                            <span v-if="book.read">Yes</span>
                            <span v-else>No</span>
                        </td>
                        <td>
                            <div class="btn-group" role="group">
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

<script>
import axios from "axios";

export default {
  data() {
    return {
      books: [],
    };
  },
  methods: {
    getBooks() {
      const path = "http://localhost:5000/books";
      axios
        .get(path)
        .then((res) => {
          console.log(res.data);
          this.books = res.data.books;
        })
        .catch((err) => {
          console.log(err.data);
        });
    },
  },
  created() {
    this.getBooks(); // Corrected method name
  },
};
</script>