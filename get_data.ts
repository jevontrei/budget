// enum APITYPE {
//     ACCOUNTS
//     TRANSACTIONS
//     PING 
// }

// async function get_data(data: UpApiType): UpReturnType {
//     switch data.ACCOUNTS { 
//         return fetch("...from accounts")
//     }
// }

/////////////////////

enum APITYPE {
    ACCOUNTS,
    TRANSACTIONS,
    PING 
}

async function get_data(data: APITYPE): UpReturnType {
    switch data.ACCOUNTS { 
        return fetch("...from accounts")
    }
}