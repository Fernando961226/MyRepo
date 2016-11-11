import json



file = open('C:\\Users\\ferna\\PycharmProjects\\untitled\\MetaData.txt', 'r')



data3='''
{
    "FirstName":"Bhairav",
    "MiddleName":"S",
    "LastName":"Ram",
    "DateOfBirth":"09-01-1984",
    "Contact":{
        "Phone":9988776655,
        "Email":"bhairav@gmail.com"
    },
    "Address":[
        {
            "Type":"Office",
            "ZipNumber":560056,
            "Street":"Nagarbhavi Road",
            "City":"Bangalore",
            "Country":"India"
        },
        {
            "Type":"Home",
            "ZipNumber":560004,
            "Street":"Gandhi Bazaar Road",
            "City":"Bangalore",
            "Country":"India"
        }
    ]
}
        '''

jsonObjectInfo = json.loads(data3)

with open('MetaData.json', 'r') as f:
    data4 = json.load(f)

print(data4)



print(format(data4['Name']))

data = {
  "Name": "OpenJMLESC",
  "DisplayName": "OpenJML (ESC)",
  "Version": "1.4",
  "Email": "jls@cs.ucf.edu",
  "SupportEmail": "jls@cs.ucf.edu",
  "TermsOfUseUrl": "http://www.openjml.org",
  "PrivacyUrl": "http://www.openjml.org",
  "Institution": "OpenJML",
  "InstitutionUrl": "http://www.openjml.org",
  "InstitutionImageUrl": "http://openjml.cs.ucf.edu/images/jml-logo-small.png",
  "MimeType": "text/plain",
  "SupportsLanguageSyntax": True,
  "Title": "A JML program verification tool (Extended Static Checking)",
  "Description": "OpenJML is a program verification tool for Java programs that allows you to check the specifications of programs annotated in the Java Modeling Language.",
  "Question": "Does this program do what it is supposed to do?",
  "Url": "http://www.openjml.org",
  "VideoUrl": None,
  "DisableErrorTable": False,
  "Samples": [
    {
      "Name": "AddLoop",
      "Source": "public class AddLoop {\n    //@ requires true;\n    //@ ensures \\result == x + y;\n    public static int AddLoop(int x, int y) {\n        int sum = x;\n        if (y > 0) {\n            int n = y;\n\n            //@ maintaining sum == x + y - n && 0 <= n;\n            //@ decreases n;\n            while (n > 0) {\n                sum = sum + 1;\n                n = n - 1;\n            }\n        } else {\n            int n = -y;\n\n            //@ maintaining sum == x + y + n && 0 <= n;\n            //@ decreases n;\n            while (n > 0) {\n                sum = sum - 1;\n\n                n = n - 1;\n            }\n        }\n        return sum;\n\n    }\n}\n"
    },
    {
      "Name": "BinarySearch",
      "Source": "public class BinarySearch {\r\n    //@ requires (\\forall int i, j; 0 <= i && i < j && j < arr.length; arr[i] <= arr[j]);\r\n    //@ ensures \\result == -1 ==> (\\forall int i; 0 <= i && i < arr.length; arr[i] != key);\r\n    //@ ensures 0 <= \\result && \\result < arr.length ==> arr[\\result] == key;\r\n    public static int BinarySearch(int[] arr, int key) {\r\n        if (arr.length == 0) {\r\n            return -1;\r\n        } else {\r\n            int low = 0;\r\n            int high = arr.length;\r\n            int mid = low + (high - low) / 2;\r\n            //@ maintaining 0 <= low && low <= high  && high <= arr.length && mid == low + (high - low) / 2;\r\n            //@ maintaining (\\forall int i; 0 <= i && i < low; arr[i] < key);\r\n            //@ maintaining (\\forall int i; high <= i && i < arr.length ==> key < arr[i]);\r\n            //@ decreases high - low;\r\n            while (low < high && arr[mid] != key) {\r\n                if (arr[mid] < key) {\r\n                    low = mid + 1;\r\n                } else {\r\n                    high = mid;\r\n                }\r\n                mid = low + (high - low) / 2;\r\n            }\r\n            if (low >= high) {\r\n                return -1;\r\n            }\r\n            return mid;\r\n        }\r\n\r\n\r\n    }\r\n}"
    },
    {
      "Name": "CopyArray",
      "Source": "public class CopyArray {\n    //@ requires a.length == b.length;\n    //@ requires 0 <= iBegin && iBegin < a.length && 0 <= iEnd && iEnd < a.length && iBegin <= iEnd;\n    //@ ensures (\\forall int i; iBegin <= i && i < iEnd; a[i] == b[i]);\n    public static void CopyArray(int[] b, int iBegin, int iEnd, int[] a) {\n        int k = iBegin;\n        ;\n        //@ maintaining iBegin <= k && k <= iEnd;\n        //@ maintaining (\\forall int i; iBegin <= i && i < k; a[i] == b[i]);\n        //@ decreases iEnd  - k;\n        while (iEnd - k > 0) {\n            a[k] = b[k];\n            k = k + 1;\n        }\n    }\n}\n"
    },
    {
      "Name": "FindFirstZero",
      "Source": "public class FindFirstZero {\n    //@ requires true;\n    //@ ensures \\result == -1 ==> (\\forall int i; 0 <= i && i < x.length; x[i] != 0);\n    //@ ensures 0 <= \\result && \\result < x.length ==> x[\\result] == 0 && (\\forall int i; 0 <= i && i < \\result; x[i] != 0);\n    public static int FindFirstZero(int[] x) {\n        assert x.length >= 0;\n        if (x.length == 0) {\n            return -1;\n        } else {\n            int index = 0;\n            //@ maintaining (\\forall int i; 0 <= i && i < index; x[i] != 0);\n            //@ maintaining (0 <= index && index <= x.length);\n            //@ decreases x.length - index;\n            while (x.length - index > 0 && x[index] != 0) {\n                index = index + 1;\n            }\n            if (x.length - index == 0) {\n                index = -1;\n            }\n            return index;\n        }\n    }\n}\n"
    },
    {
      "Name": "Inverse",
      "Source": "// It specifies and verifies that the array a is an inverse of the array b\r\npublic class Inverse {\r\n    //@ requires true;\r\n    //@ ensures \\result == false ==> ((x.length != y.length) || (\\exists int i; 0 <= i && i < x.length; x[i] != y[x.length - 1 -i]));\r\n    //@ ensures \\result == true ==> x.length == y.length && (\\forall int i; 0 <= i && i < x.length; x[i] == y[x.length - 1 - i]);\r\n    public static boolean Inverse(int[] x, int[] y) {\r\n        if (x.length != y.length) return false;\r\n        assert x.length == y.length;\r\n        int index = 0;\r\n        //@ maintaining 0 <= index && index <= x.length && x.length == y.length;\r\n        //@ maintaining (\\forall int i; 0 <= i && i < index; x[i] == y[x.length -1 - i]);\r\n        //@ decreases x.length - index;\r\n        while (index < x.length) {\r\n            if (x[index] != y[x.length - 1 - index]) {\r\n                return false;\r\n            } else {\r\n                index = index + 1;\r\n            }\r\n        }\r\n        return true;\r\n    }\r\n}"
    },
    {
      "Name": "Smallest",
      "Source": "public class Smallest {\r\n    //@ requires true;\r\n    //@ ensures \\result == -1 ==> a.length == 0;\r\n    //@ ensures \\result > -1 ==> (\\forall int i; 0 <= i && i < a.length; a[\\result] <= a[i]);\r\n    static public int Smallest(int[] a) {\r\n        if (a.length == 0) return -1;\r\n\r\n        int index = 0;\r\n        int smallest = 0;\r\n        //@ maintaining 0 <= index && index <= a.length;\r\n        //@ maintaining 0 <= smallest && smallest < a.length;\r\n        //@ maintaining (\\forall int i; 0 <= i && i < index; a[smallest] <= a[i]);\r\n        //@ decreases a.length - index;\r\n        while (a.length - index > 0) {\r\n            if (a[index] < a[smallest]) {\r\n                smallest = index;\r\n            }\r\n            index = index + 1;\r\n        }\r\n        return smallest;\r\n    }\r\n}\r\n"
    }
  ],
  "Tutorials":None
}


jsonData = json.dumps(data)
print(jsonData)