import axios from "axios";
import { ref, computed } from "vue";
import { defineStore } from "pinia";

export const usePostStore = defineStore("post", () => {
  const posts = ref([]);
  const getPosts = function () {
    axios({
      method: "get",
      url: "http://127.0.0.1:8000/api/v1/posts/",
    })
      .then((res) => {
        console.log(res);
        posts.value = res.data;
      })
      .catch((err) => {
        console.log(err);
      });
  };
  return { posts, getPosts };
});
