import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";

export const useCounterStore = defineStore(
  "counter",
  () => {
    const articles = ref([]);
    const API_URL = "http://127.0.0.1:8000";

    // DRF로 전체 게시글 조회 요청을 보내고 응답을 받아 articles에 저장하는 함수
    const getArticles = function () {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/articles/`,
      })
        .then((response) => {
          // console.log(response);
          articles.value = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    };
    return { articles, API_URL, getArticles };
  },
  { persist: true }
);
