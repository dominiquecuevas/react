function Mailbox(props) {
    const unreadMessages = props.unreadMessages;
    return (
        <div>
            <h1>Hello!</h1>
            {unreadMessages.length > 0 &&
                <h2>
                    You have {unreadMessages.length} unread messages.
                </h2>
            }
        </div>
    );
}

const messages = ['Message1', 'Re: Message1', 'Fwd: Re: Message1']
ReactDOM.render(
    <Mailbox unreadMessages={messages} />,
    document.getElementById('root')
);