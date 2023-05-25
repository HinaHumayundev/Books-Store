<template>
    <div class="jumbotron-vertical-center">
    <div class="container">
        <!-- bootswatch CDN -->
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/slate/bootstrap.min.css" integrity="sha384-8iuq0iaMHpnH2vSyvZMSIqQuUnQA7QM+f6srIdlgBrTSEyd//AWNMyEaSF2yPzNQ" crossorigin="anonymous">
        <div class="row">
            <div class="col-sm-12">
              <h1 class="text-center bg-primary" style="background: linear-gradient(to right, #b3c2e0, #6598fd,  #1a1a1b);border-radius:16px; font-family: 'Arial', sans-serif; color: #ffffff;">Book Library 📚</h1>

                <hr><br>
                <b-alert variant="success" v-if="showMessage" show> {{ message }}
                </b-alert>
                <button type="button" style="background: linear-gradient(to right, #b3c2e0, #1a1a1b); color:#ffffff;" class="btn btn-sm" @click="$refs.addBookModal.show()">Add Book</button>
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
                                <button type="button" class="btn btn-info btn-sm" v-modal.book-update-modal @click="editBook(book)">Update</button>
                                <button type="button" class="btn btn-danger btn-sm">Delete</button>
                            </div>
                        </td>
                    </tr>
                   </tbody>
                </table>
                <footer class="bg-primary text-center" style="border-radius:10px;" >Made by Hina Humayun</footer>
 
            </div>
        </div>
        <!-- Fist Modal -->
        <b-modal ref="addBookModal"
        id="book-modal" 
        title="Add a new book" hide-backdrop hide-footer>
        <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        <!-- Add Title -->
        <b-form-group id="form-title-group" label="Title:" label-for="form-title-input">
        <b-form-input id="form-title-input" type="text" v-model="addBookForm.title" required placeholder = "Enter Book">

        </b-form-input>
        </b-form-group>
        <!-- Add Genre -->
        <b-form-group id="form-genre-group" label="Genre:" label-for="form-genre-input">
        <b-form-input id="form-genre-input" type="text" v-model="addBookForm.genre" required placeholder = "Enter Genre">

        </b-form-input>
        </b-form-group>

         <!-- Read? -->
         <b-form-group id="form-read-group" label-for="form-read-checkbox">
         <b-form-checkbox-group id="form-read-checkbox" v-model="addBookForm.read">
         <b-form-checkbox value="read">Read</b-form-checkbox>
          </b-form-checkbox-group>
           </b-form-group>

         <b-button type="submit" variant="outline-info">Submit</b-button>
         <b-button type="reset" variant="outline-danger">Reset</b-button>
        </b-form>
      </b-modal>


      <!-- Second Modal -->
      <b-modal ref="editBookModal"
        id="book-update-modal" 
        title="Update" hide-backdrop hide-footer>
        <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
        <!-- Add Title -->
        <b-form-group id="form-title-edit-group" label="Title:" label-for="form-title-edit-input">
        <b-form-input id="form-title-edit-input" type="text" v-model="editForm.title" required placeholder = "Enter title">

        </b-form-input>
        </b-form-group>
        <!-- Add Genre -->
        <b-form-group id="form-genre-edit-group" label="Genre:" label-for="form-genre-edit-input">
        <b-form-input id="form-genre-edit-input" type="text" v-model="editForm.genre" required placeholder = "Enter Genre">

        </b-form-input>
        </b-form-group>

         <!-- Read? -->
         <b-form-group id="form-read-edit-group" label-for="form-read-edit-checkbox">
         <b-form-checkbox-group id="form-read-ediy-checkbox" v-model="editForm.read">
         <b-form-checkbox value="read">Read</b-form-checkbox>
          </b-form-checkbox-group>
           </b-form-group>

         <b-button type="submit" variant="outline-info">Submit</b-button>
         <b-button type="reset" variant="outline-danger">Reset</b-button>
        </b-form>
      </b-modal>


      <!--  -->
    </div>
</div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      books: [],
      addBookForm: {
        title : "",
        genre : "",
        read :[],
      },
      message: "",      
      showMessage: false,
      editForm :{
        BookId: "",
        title : "",
        genre : "",
        read :[],
      }

    };
  },

  message : "",
  methods: {
    //GET Function
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

    addBooks(payload) {
  const path = "http://localhost:5000/books";
  axios
    .post(path, payload)
    .then(() => {
      this.getBooks();
      this.message =" Book Added!";
      this.showMessage = true;
      setTimeout(() => {
        this.showMessage = false;
      }, 3000);
    })
    .catch((err) => {
      console.log(err.data);
      this.getBooks();
    });
},

    //Used while entering a new book
    initForm() 
    {
      this.addBookForm.title = "";
      this.addBookForm.genre = "";
      this.addBookForm.read = [];
    },
    onSubmit(e) {
      e.preventDefault();
      this.$refs.addBookModal.hide();
      let read = false;
      if (this.addBookForm.read[0]) read = true;
      const payload = {
        title : this.addBookForm.title,
        genre: this.addBookForm.genre,
        read,
      };
      this.addBooks(payload);
      this.initForm();
    },
    onReset(e) {
      e.preventDefault();
      this.$refs.addBookModal.hide();
      this.initForm();
    }
  },
  created() {
    this.getBooks(); // Corrected method name
  },
};
</script>