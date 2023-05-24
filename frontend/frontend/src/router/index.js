import Vue from "vue";
import VueRouter from "vue-router";
import Shark from "../components/Shark.vue";
import BooksComponent from "../components/BooksComponent.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/shark",
    name: "SharkComponent",
    component: Shark,
  },
  {
    path: "/books",
    name: "BooksComponent",
    component: BooksComponent,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
