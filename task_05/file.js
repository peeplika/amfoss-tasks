class Header extends HTMLElement {
  connectedCallback() {
    const shadow = this.attachShadow({ mode: 'open' });
    const style = document.createElement('style');
    style.textContent = `
     .navbar {
  background-color: rgba(11, 11, 33, 1);
  color: white; 
  position: fixed;
  width: 100%;
  z-index: 1000;
}

.navbar ul {
  list-style: none;
  display: flex;
  margin: 10px;
  justify-content: flex-end; 
}

.navbar a {
  text-decoration: none;
  color: white;
  font-weight: bold;
  font-size: 16px; 
  opacity: 0.5; 
  display: inline-block; 
  height: 20px; 
  width: 20px; 
}
.navbar a:hover {
  text-decoration: underline;
  opacity: 1; 
}

.icon {
  background-size: contain; 
  background-repeat: no-repeat;
  height: 30px; 
  width: 30px; 
  margin:10px;
}


.logo {
  margin-right: auto; 
}

.logo img {
  height: 40px; 
  width: auto; 
  display: block;
}
    `;
    const nav = document.createElement('nav');
    nav.innerHTML = `
      <div class="navbar">
        <ul>
          <li class="logo"><img src="assets/navbar/logo.png" alt="Logo"><a href="index.html"></a></li>
          <li class="icon" style="background-image: url('assets/navbar/spotify.png');"><a href="https://open.spotify.com/artist/53XhwfbYqKCa1cC15pYq2q"></a></li>
          <li class="icon" style="background-image: url('assets/navbar/youtube.svg');"><a href="https://www.youtube.com/channel/UCT9zcQNlyht7fRlcjmflRSA"></a></li>
          <li class="icon" style="background-image: url('assets/navbar/twitter.svg');"><a href="https://twitter.com/imaginedragons?lang=en"></a></li>
          <li class="icon" style="background-image: url('assets/navbar/instagram.svg');"><a href="https://www.instagram.com/imaginedragons/"></a></li>
        </ul>
      </div>
    `;

  
    shadow.appendChild(style);
    shadow.appendChild(nav);
  }
}

customElements.define('main-header', Header);

