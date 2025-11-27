import React, { useState, useEffect } from 'react';
import styles from './styles.module.css';

const ChatWidget = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [isClient, setIsClient] = useState(false);
  const [selection, setSelection] = useState(null);
  const [tooltipPosition, setTooltipPosition] = useState({ top: 0, left: 0 });

  useEffect(() => {
    setIsClient(true);
  }, []);

  const handleMouseUp = () => {
    const selectedText = window.getSelection().toString().trim();
    if (selectedText) {
      const range = window.getSelection().getRangeAt(0);
      const rect = range.getBoundingClientRect();
      setSelection(selectedText);
      setTooltipPosition({
        top: rect.bottom + window.scrollY + 5,
        left: rect.left + window.scrollX + rect.width / 2,
      });
    } else {
      setSelection(null);
    }
  };

  const handleAskAi = () => {
    setIsOpen(true);
    // Here you would pass the selection to the chat logic
    console.log("Selected text:", selection);
    setSelection(null);
  };

  useEffect(() => {
    document.addEventListener('mouseup', handleMouseUp);
    return () => {
      document.removeEventListener('mouseup', handleMouseUp);
    };
  }, []);

  const toggleChatWindow = () => {
    setIsOpen(!isOpen);
    setSelection(null); // Close tooltip when chat is opened/closed
  };

  if (!isClient) {
    return null;
  }

  return (
    <>
      {selection && (
        <div
          className={styles.tooltip}
          style={{ top: tooltipPosition.top, left: tooltipPosition.left }}
          onClick={handleAskAi}
        >
          Ask AI
        </div>
      )}
      <div className={styles.launcherButton} onClick={toggleChatWindow}>
        <span>💬</span>
      </div>
      {isOpen && (
        <div className={styles.chatWindow}>
          <div className={styles.chatHeader}>
            <h2>Chat</h2>
            <button onClick={toggleChatWindow} className={styles.closeButton}>
              ✕
            </button>
          </div>
          <div className={styles.messageArea}>
            <p>Chat window content goes here.</p>
          </div>
          <div className={styles.inputField}>
            <input type="text" placeholder="Type a message..." />
            <button>Send</button>
          </div>
        </div>
      )}
    </>
  );
};

export default ChatWidget;