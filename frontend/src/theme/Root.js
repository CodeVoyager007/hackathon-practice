import React from 'react';
import FloatingChatWidget from '@site/src/components/FloatingChatWidget';

export default function Root({children}) {
  return (
    <>
      {children}
      <FloatingChatWidget />
    </>
  );
}
