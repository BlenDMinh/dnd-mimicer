import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router";
import Layout from "./components/Layout";
import Home from "./pages/Home";
import About from "./pages/About";
import Users from "./pages/Users";
import Channels from "./pages/Channels";
import CronJobs from "./pages/CronJobs";

const App: React.FC = () => {
  return (
    <Router>
      <Layout>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
          <Route path="/users" element={<Users />} />
          <Route path="/channels" element={<Channels />} />
          <Route path="/cronjobs" element={<CronJobs />} />
        </Routes>
      </Layout>
    </Router>
  );
};

export default App;
