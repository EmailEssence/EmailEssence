/* eslint-disable react/prop-types */
import {useState} from "react";
import InboxIcon from "../../assets/InboxIcon";
import SettingsIcon from "../../assets/SettingsIcon";
import "./sidebar.css";

const unselectedColor = "#1E1E1E";
const selectedColor = "#D9D9D9";
const unselectedColorInner = "#E9E9E9";
const selectedColorInner = "#1E1E1E";
const sideBarContracted = "80px";

export default function SideBar({onLogoClick, containerWidth}) {
  const [selected, setSelected] = useState("logo");

  const handleClick = useStateID => {
    //sets the selected state ID to dashboard after being unselected
    if (selected === useStateID) {
      setSelected("logo");
      return;
    }
    setSelected(useStateID);
  };

  return (
    <div>
      <div className="sidebar" style={{width: containerWidth}}>
        <LogoButton
          containerWidth={containerWidth}
          curState={selected}
          onClick={() => {
            handleClick("logo");
            onLogoClick();
          }}
        />
        <InboxButton
          containerWidth={containerWidth}
          curState={selected}
          onClick={() => handleClick("inbox")}
        />
        <p></p>
        <SettingsButton
          containerWidth={containerWidth}
          curState={selected}
          onClick={() => handleClick("settings")}
        />
      </div>
    </div>
  );
}

function LogoButton({containerWidth, curState, onClick}) {
  const color = curState === "logo" ? selectedColor : unselectedColor;
  return (
    <div>
      <div
        className="container"
        id="logo"
        onClick={onClick}
        style={{
          backgroundColor: color,
          width: containerWidth,
        }}
      >
        <p>EmailESSENCE</p>
      </div>
    </div>
  );
}

function InboxButton({containerWidth, curState, onClick}) {
  const text = containerWidth === sideBarContracted ? "" : "Inbox";
  const color = curState === "inbox" ? selectedColor : unselectedColor;
  const innerColor =
    curState === "inbox" ? selectedColorInner : unselectedColorInner;
  return (
    <div>
      <div
        className="container"
        id="inbox"
        onClick={onClick}
        style={{backgroundColor: color, width: containerWidth}}
      >
        <div className="icon">
          <div>
            <InboxIcon color={innerColor} />
          </div>
          <p style={{color: innerColor}}>{text}</p>
        </div>
      </div>
    </div>
  );
}

function SettingsButton({containerWidth, curState, onClick}) {
  const text = containerWidth === sideBarContracted ? "" : "Settings";
  const color = curState === "settings" ? selectedColor : unselectedColor;
  const innerColor =
    curState === "settings" ? selectedColorInner : unselectedColorInner;
  return (
    <div>
      <div
        className="container"
        id="settings"
        onClick={onClick}
        style={{
          backgroundColor: color,
          width: containerWidth,
        }}
      >
        <div className="icon">
          <div>
            <SettingsIcon color={innerColor} />
          </div>
          <p style={{color: innerColor}}>{text}</p>
        </div>
      </div>
    </div>
  );
}
