/* eslint-disable react/prop-types */
//import "./emailDisplay.css";
import "./emailEntry.css";
import "./emailList.css";
import {useState} from "react";
import {emails} from "../../emails/emails";

export default function Inbox() {
  const [curEmail, setCurEmail] = useState(0);
  const handleClick = email => {
    setCurEmail(email);
  };
  return (
    <div className="inbox-display">
      <InboxEmailList curEmail={curEmail} onClick={handleClick} />
      <EmailDisplay key={curEmail} curEmail={curEmail} />
    </div>
  );
}

function EmailEntry({email, onClick, selected}) {
  const content = emails[email];
  const brColor = selected ? "#D9D9D9" : "#FFFFFF";
  return (
    <div className="entry" style={{backgroundColor: brColor}} onClick={onClick}>
      <div className="indicator-container">
        <div className="indicator"></div>
      </div>
      <div className="head">
        <div className="from">{content.from}</div>
        <div className="date">{content.date}</div>
      </div>
      <div className="title">{content.title}</div>
      <div className="separator-container">
        <div className="separator"></div>
      </div>
      <div className="summary">{content.summary}</div>
    </div>
  );
}

function InboxEmailList({curEmail, onClick}) {
  const emails = () => {
    const returnBlock = [];
    for (let i = 0; i < 20; i++) {
      let selected = i === curEmail;
      returnBlock.push(
        <EmailEntry
          key={i}
          email={i}
          onClick={() => onClick(i)}
          selected={selected}
        />
      );
    }
    return returnBlock;
  };
  return (
    <div className="list">
      <div className="inbox-title-container">
        <div className="inbox-title">
          <div className="inbox-icon">IN</div>
          <div className="inbox-word">Inbox</div>
        </div>
      </div>
      <div className="divider"></div>
      <div className="email-container">
        <div className="emails">{emails()}</div>
      </div>
    </div>
  );
}

function EmailDisplay({curEmail}) {
  const curContent = emails[curEmail];
  return (
    <div className="email-display">
      <div className="header">
        <div className="from">{curContent.from}</div>
        <div className="title">{curContent.title}</div>
        <div className="to">{curContent.to}</div>
        <div className="date">{curContent.date}</div>
        <ReaderView curEmail={curEmail} />
      </div>
      <div className="body">
        <div className="content">{curContent.content}</div>
      </div>
    </div>
  );
}

function ReaderView({curEmail}) {
  console.log(curEmail);
  return <div></div>;
}
