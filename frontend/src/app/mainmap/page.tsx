'use client';

import { useEffect, useState } from 'react';

export default function MainMapPage() {
    const [socket, setSocket] = useState<WebSocket | null>(null);
    const [messages, setMessages] = useState<string[]>([]);
    const [input, setInput] = useState('');
    const [role, setRole] = useState<string | null>(null);
    

    useEffect(() => {
        const storedRole = sessionStorage.getItem('role');
        setRole(storedRole);
        // WEB SOCKETS DISABLED FOR NOW
        /*
        const ws = new WebSocket('ws://localhost:8000/ws/mainmap/');
        setSocket(ws);

        ws.onmessage = (event) => {
            try {
                const msg = JSON.parse(event.data);
                setMessages((prev) => [...prev, msg.message]); // 👈 extract "message" key
            } catch (e) {
                console.error('Invalid JSON received:', event.data);
            }
        };

        ws.onclose = () => {
            console.log('WebSocket disconnected');
        };

        return () => {
            ws.close();
        };
        */
    }, []);

    // used for sending messages over websockets - currently not in use
    const sendMessage = () => {
        if (socket && socket.readyState === WebSocket.OPEN) {
            const payload = JSON.stringify({ message: input });
            socket.send(payload);
            setInput('');
        }
    };

    return (
        <div className="flex h-screen w-screen bg-neutral-900 text-white relative">
            {/* Main content */}
            <div className="flex flex-row w-full h-full z-10 p-4 space-x-4">
                {/* Map Panel */}
                <div className="w-[70%] h-full bg-neutral-800 rounded-lg overflow-hidden">
                    <img
                        src="/maps/taiwan_middle_hex.png"
                        alt="Map"
                        className="object-contain w-full h-full"
                    />
                </div>

                {/* Placeholder UI Panel */}
                <div className="flex-1 h-full bg-neutral-800 rounded-lg p-4">
                    <h2 className="text-lg mb-2">Current Role: {role || 'Unknown'}</h2>
                    <p className="text-gray-300">Future UI space: devices, logs, etc.</p>
                </div>
            </div>
        </div>
    );
}
