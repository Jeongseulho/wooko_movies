<template>
  <section id="nav-bar">
    <section id="top">
      <div class="container">
        <div class="row top_1">
          <div class="col-md-3">
            <div class="top_1l pt-1">
              <h3 class="mb-0">
                <router-link
                  :to="{ name: 'home' }"
                  style="text-decoration: none; color: var(--bs-red)"
                  ><i class="fa fa-video-camera col_red me-1"></i>WOOKO
                  MOVIES</router-link
                >
              </h3>
            </div>
          </div>
          <div class="col-md-5">
            <div class="top_1m">
              <div class="input-group">
                <input
                  type="text"
                  class="form-control bg-black"
                  placeholder="Search Site..."
                  v-model="keyword"
                  @keyup.enter="search"
                />
                <span class="input-group-btn">
                  <button
                    @click="search"
                    class="btn text-white rounded-0 bg-danger"
                    type="button"
                  >
                    Search
                  </button>
                </span>
              </div>
            </div>
          </div>
          <div class="col-md-4 text-end">
            <router-link
              v-if="!isLogin"
              class="button text-decoration-none"
              :to="{ name: 'login' }"
            >
              Login</router-link
            >
            <button
              v-else
              class="button text-decoration-none"
              @click="fetchLogout"
            >
              Logout
            </button>
          </div>
        </div>
      </div>
    </section>

    <section id="header">
      <nav class="navbar navbar-expand-md navbar-light" id="navbar_sticky">
        <div class="container">
          <button
            class="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav mb-0">
              <li class="nav-item">
                <router-link class="nav-link" :to="{ name: 'home' }"
                  >HOME</router-link
                >
              </li>
              <li class="nav-item" v-if="isLogin">
                <router-link class="nav-link" :to="{ name: 'community' }"
                  >COMMUNITY</router-link
                >
              </li>

              <li class="nav-item dropdown" v-if="isLogin">
                <a
                  class="nav-link dropdown-toggle"
                  href="#"
                  id="navbarDropdown"
                  role="button"
                  data-bs-toggle="dropdown"
                  aria-expanded="false"
                >
                  MINI GAME
                </a>
                <ul
                  class="dropdown-menu drop_1"
                  aria-labelledby="navbarDropdown"
                >
                  <li>
                    <router-link
                      class="dropdown-item"
                      :to="{ name: 'worldcup', params: { round: 8 } }"
                      >이상형 월드컵(8강)</router-link
                    >
                  </li>
                  <li>
                    <router-link
                      class="dropdown-item"
                      :to="{ name: 'worldcup', params: { round: 16 } }"
                      >이상형 월드컵(16강)</router-link
                    >
                  </li>
                  <li>
                    <router-link
                      class="dropdown-item"
                      :to="{ name: 'worldcup', params: { round: 32 } }"
                      >이상형 월드컵(32강)</router-link
                    >
                  </li>
                  <li>
                    <router-link
                      class="dropdown-item border-0"
                      :to="{
                        name: 'versus-game-movie',
                      }"
                      >VS 게임(영화 ver)</router-link
                    >
                  </li>
                  <li>
                    <router-link
                      class="dropdown-item border-0"
                      :to="{
                        name: 'versus-game-actor',
                      }"
                      >VS 게임(배우 ver)</router-link
                    >
                  </li>
                  <li>
                    <router-link
                      class="dropdown-item border-0"
                      :to="{
                        name: 'versus-game-director',
                      }"
                      >VS 게임(감독 ver)</router-link
                    >
                  </li>
                </ul>
              </li>
              <li class="nav-item" v-if="isLogin">
                <router-link
                  class="nav-link"
                  :to="{ name: 'profile', params: { userId: getCurUser.pk } }"
                  >MY PROFILE</router-link
                >
              </li>
            </ul>
          </div>
        </div>
      </nav>
    </section>
  </section>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
export default {
  name: 'NavBar',
  data() {
    return {
      keyword: '',
    };
  },
  computed: {
    ...mapGetters(['getSearchedMovies', 'isLogin', 'getCurUser']),
  },

  methods: {
    ...mapActions(['fetchSearchMovies', 'fetchLogout']),

    search() {
      if (this.keyword === '') return alert('검색어를 입력해주세요.');

      this.$router.push({
        name: 'movie-search',
        params: { keyword: this.keyword },
      });
      this.keyword = '';
    },
  },
};
</script>

<style></style>
