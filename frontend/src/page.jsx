import { useState } from "react";
import Dashboard from "./components/dashboard/dashboard";
import Inbox from "./components/inbox/inbox";
import { Login } from "./components/login/login";
import Register from "./components/register/register";
import { Settings } from "./components/settings/settings";
import SideBar from "./components/sidebar/sidebar";
import { markEmailAsRead } from "./emails/emailHandler";
import fetchEmails from "./emails/emailParse";
import "./page.css";

export default function Page() {
  const [curPage, setCurPage] = useState("login");
  const [expandedSideBar, setExpandedSideBar] = useState(false);
  const [loggedIn, setLoggedIn] = useState(false);
  const [curEmail, setCurEmail] = useState(null);
  const [isChecked, setIsChecked] = useState(false);
  const [emailFetchInterval, setEmailFetchInterval] = useState(0);
  const [theme, setTheme] = useState("system");
  const [emailsByDate, setEmailsByDate] = useState(null);
  const gridTempCol = `${expandedSideBar ? "180" : "80"}px 1fr`;

  const handleLogin = () => {
    setLoggedIn(true);
    setEmailsByDate(fetchEmails());
    setCurEmail(emailsByDate[0]);
    setCurPage("dashboard");
  };

  // Function to handle expanding and collapsing of sidebar
  const handleLogoClick = () => {
    setExpandedSideBar(!expandedSideBar);
  };

  const handlePageChange = (pageName) => {
    curPage === pageName ? setCurPage("dashboard") : setCurPage(pageName);
  };

  const handleSetCurEmail = (email) => {
    setCurEmail(email);
    if (!email.is_read) markEmailAsRead(email);
  };

  const handleToggleSummariesInInbox = () => {
    setIsChecked(!isChecked);
  };

  const handleSetEmailFetchInterval = (interval) => {
    setEmailFetchInterval(interval);
  };

  const handleSetTheme = (theme) => {
    setTheme(theme);
  };

  const getPage = () => {
    switch (curPage) {
      case "inbox":
        return (
          <Inbox
            emailList={emailsByDate}
            setCurEmail={handleSetCurEmail}
            curEmail={curEmail}
          />
        );
      case "settings":
        return (
          <Settings
            isChecked={isChecked}
            handleToggleSummariesInInbox={handleToggleSummariesInInbox}
            emailFetchInterval={emailFetchInterval}
            handleSetEmailFetchInterval={handleSetEmailFetchInterval}
            theme={theme}
            handleSetTheme={handleSetTheme}
          />
        );
      default:
        return (
          <Dashboard
            emailList={emailsByDate}
            handlePageChange={handlePageChange}
            setCurEmail={handleSetCurEmail}
          />
        );
    }
  };

  const emailClient = () => {
    return (
      <div className="client" style={{ gridTemplateColumns: gridTempCol }}>
        <SideBar
          onLogoClick={handleLogoClick}
          expanded={expandedSideBar}
          handlePageChange={handlePageChange}
          selected={curPage}
        />
        {getPage()}
      </div>
    );
  };

  const loginPage = () => {
    return (
      <Login
        forward={handleLogin}
        // onSignUpClick={() => setCurPage("register")}
      />
    );
  };

  const registerPage = () => {
    return <Register onLoginClick={() => setCurPage("login")} />;
  };

  return (
    <>
      <div className="page">
        {loggedIn
          ? emailClient()
          : curPage === "login"
          ? loginPage()
          : registerPage()}
      </div>
    </>
  );
}
