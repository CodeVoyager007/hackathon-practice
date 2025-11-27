import React, { useState, useEffect, useRef } from 'react';
import Chatbot from '@site/src/components/Chatbot';
import styles from './styles.module.css';

const ChatWrapper = ({ children }) => {
  const [isOpen, setIsOpen] = useState(false);
  const [selection, setSelection] = useState(null);
  const [tooltipPosition, setTooltipPosition] = useState({ top: 0, left: 0 });

  const handleMouseUp = () => {
    const selectedText = window.getSelection().toString().trim();
    if (selectedText) {
      const range = window.getSelection().getRangeAt(0);
      const rect = range.getBoundingClientRect();
      setSelection(selectedText);
      setTooltipPosition({
        top: rect.bottom + window.scrollY,
        left: rect.left + window.scrollX + rect.width / 2,
      });
    } else {
      setSelection(null);
    }
  };

  const handleAskAi = () => {
    setIsOpen(true);
    // We will need to pass this selection to the chatbot
    // For now, let's just open the chat
    setSelection(null);
  };

  useEffect(() => {
    document.addEventListener('mouseup', handleMouseUp);
    return () => {
      document.removeEventListener('mouseup', handleMouseUp);
    };
  }, []);

  const toggleChat = () => {
    setIsOpen(!isOpen);
  };

  return (
    <>
      {children}
      {selection && (
        <div
          className={styles.tooltip}
          style={{ top: tooltipPosition.top, left: tooltipPosition.left }}
          onClick={handleAskAi}
        >
          Ask AI
        </div>
      )}
      <div className={styles.chatIcon} onClick={toggleChat}>
        💬
      </div>
      
      <div className={`${styles.chatDialog} ${isOpen ? styles.open : ''}`}>
        <div className={styles.chatDialogHeader}>
          <h3>AI Assistant</h3>
          <button onClick={toggleChat} className={styles.closeButton}>×</button>
        </div>
        <Chatbot selection={selection} />
      </div>
    </>
  );
};

export default ChatWrapper;