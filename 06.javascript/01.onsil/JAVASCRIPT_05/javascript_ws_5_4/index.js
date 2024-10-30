/* 
  아래에 코드를 작성해주세요.
*/

const searchBtn = document.querySelector(".search-box__button");

const fetchAlbums = function (page = 1, limit = 10) {
  // alert("확인!");
  const keyword = document.querySelector(".search-box__input").value;

  axios({
    method: "get",
    url: "http://ws.audioscrobbler.com/2.0/",
    params: {
      method: "album.search",
      limit: limit,
      page: page,
      album: keyword,
      api_key: "87651ae2ff40b4ea48d773540d841ff9",
      format: "json",
    },
  })
    .then((response) => {
      const albums = response.data.results.albummatches.album;
      console.log(albums);
      return albums;
    })
    .then((albums) => {
      for (album of albums) {
        const cardImg = document.createElement("img");
        cardImg.src = album.image[1]["#text"];

        const card = document.createElement("div");
        card.classList.add("search-result__card");
        card.append(cardImg);

        // search-result__text
        const cardText = document.createElement("div");
        cardText.classList.add("search-result__text");
        const artistName = document.createElement("h2");
        artistName.textContent = album.artist;
        cardText.appendChild(artistName);
        const albumName = document.createElement("p");
        albumName.textContent = album.name;
        cardText.appendChild(albumName);
        card.appendChild(cardText);

        const searchResult = document.querySelector(".search-result");
        searchResult.appendChild(card);
      }
    })
    .catch((error) => alert("잠시 후 다시 시도해주세요."));
};

searchBtn.addEventListener("click", fetchAlbums);
