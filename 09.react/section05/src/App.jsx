import './App.css'
import Header from "./components/Header.jsx";   // 파일 확장자까지 안써도 됨
import Main from './components/Main.jsx'
import Footer from './components/Footer.jsx'



function App() {

  return (
    <>
    <Header />
    <Main />
    <Footer />
      {/* <h1>안녕, 리액트!!</h1> */}
    </>
  )
}

export default App
