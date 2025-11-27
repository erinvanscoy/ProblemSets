%% Comment - Erin Vanscoy PSYC 5P02 Notes Week 10

%{} Typing Path - the matlab path that are displayed currently 

% To add something to your path - can type addpath(genpath(~/documents)
 

%% Notes from last class - followup 
% myVar = [1,2,3,4,5; 6 7 8 9 10] - 5x2 - rows have to be the same dimensions,
% (same amount of elements) 
% Indexing - myVar(2,3) - indexing the second section and thrid number 
% Indexing starts at 1 not 0 
% If wanted to index the entire first section - myVar(1,:) 
% newVar = myVar'- this will switch it to 2x5 instead of 5x2 
% myVar(2,6) = 11 - adds 11 to the list but also adds a 0, because it has
% myVar(:,6) = [] - will delete the Nan and 11 values [] - delete 
% if you type save (it will prompt you with the file name) 
% Load command - type in your file name will than load all the varibles you created
% in that file 
% Matlab does matrix math, which is difference than item math - need to
% make sure you are either doing a matix of item math (not the same!!) 

%help function-name (this is the help function, can call it on any
%function) 

%% Logical operations 
% e.g., 1 == 0 (1 is equal to 0) - will print out automatically (logical) if you
% dont add a semi-colon(;) 
% If statment (starts with if and ends with end) - indenting does not
% matter!!

% % Lesson 9 - in class exercises
%% 9.1 - making if statements
% Let's start by shuffling the rng
rng('shuffle');

a = rand();
myVar = 1==1;

if a < 0.3  %if the value a is less than .33 (if it returns true)
    b = a.^2;  %square
elseif a >= 0.33 && a <= .66  % here it is elseif - use & instead of and  
    another = true;
    b = 0;
else % if everything returned false - note you dont need a colon 
    b = a.^.5; %squareroot
end %the end of my first if statment 

%% 9.2 - Switch/case

k = randi(6); % make a variable (random number between 0-6) 

switch k %start of switch
    case {1,2} % if case is 1,2 it is low etc 
        VWMCapacity = 'low';
    case {3,4}
        VWMCapacity = 'med';
    otherwise
        VWMCapacity = 'high';  
    end % end of switch

%% 9.3 - For Loops


var = 11:21 % create a vector

for i = 1:length(var) %loop through elements of that vector, i will start at 1 and then loop through all the range
    
    i
    var(i)
    a = var(i)^2
    
end % loop

% Note - edit command (edit(filename) - will open up your file

%% 9.4 comparing indexing to loops

tic % start clock, record how long it takes to evaluate between tic and tok 
a = zeros(1,10); % pre-allocating a variable 
toc %end clock

b = [];
tic
for i = 1:10
    b(i) = i^2; %adding elements to b
end
toc

tic
for i = 1:10
    a(i) = i^2; %inserting elements into pre-allocated a
end
toc


%% 9.5 Embedding while loops

numLoops = 0;
a = 0;        %give it a start value
numLoops2 = 0;
numLoops3 = 0;

while a < .9    %make it meat some condition - as long as a is > .9, the loop will run forever 
numLoops = numLoops + 1;
a = rand();  %reset value of a
if a < .5
numLoops2 = numLoops2 + 1;
if a < .1 % if you select the if, it will show you the corresponding end for that statment 
continue; % continue will continue onto the next section of code 
numLoops3 = numLoops3 + 1;     
end %who do these belong to?
end % should make notes as to where things (loops if statments) start and end 
if a == .7    %here's an if statement that will break out of the loop
break; % Exist completely out of the loop 
end % who do these belong to??
end %c 


% Parfor - allows you to run loops in parallel rather than in sequence 
%% 9. 6 -  indexing


x = round(10 + randn(100,1));  %random normal numbers centered on 10, create random 100 values and round them and then add 10 

(x==10) % return boolean mask of location, 1 = true (value =10), 0=false (value not equal to 10)
x(x==10) % Returning value of x, when equal to x (will just return back 10s)
find(x==10)% find locations in original varibles where location is equal to 10 

%any and all

any(x==10) % will return is any is equal to 10 

all(x==10) % will return is all is equal to 10 

%% 9.7 - Functions
% Part of a larger script or a stand alone script, things we can do to pass
% varibles in and out and be more efficient 
% 

function myfcn(arg1,arg2,arg3)
if nargin < 3
    arg3 = some_value;
end;
if nargin < 2
    arg2 = some_other_value;
end;
end;

% Specify the output varibles in the definintions of the function 

%% Function e.g., x2 from class 

function outputarray = subtractone(inputarray) % saving this as an .md file will make it a global function, right now its only local (if keep local define it at the top of your scipt) 
outputarray = inputarray - 1;
end 
% Initialize a cell array to store results for each array restults 

% call function - subtractone(10:3:33) - start at 10, go up by 3, until you
% hit 33 (this function will subtract 1) 


% Inside your function, varibales are local unless specified to return 

subjectnum = input('Please enter the subject number:'); 
% This will display input and store the subject number is subjectnum 


%% 9.8 - text

% my text = ('input text') - how to apply string to a varible, it is class
% char 
% can index the varible like mytext(7) and will display back the 7th
% character 
% double(mytext) function - it will return back the values based on which number
% they are, - converts the string into numbers 
% char(mytext) function - will return back to string 

%comparing strings:
'apples' == 'oranges' % single quotes will compare element by element (wont work here), but if you do double quotes it wil compare them 
strcmp('apples', 'oranges') %this is a string comparer function - 

%can ignore case with strcmpi

%string find:

strfind('where in the world is carmen sandiego', 'carmen sandiego') % if you want to find something in a string, it will tell you if it exists 

%string replace:

strrep('a a a a ', ' ', []) 

% $s - means to interpret it as a string 

% writing to a file:

fid = fopen('myFile.txt', 'wt');
rr = 1.1:5.1;

fprintf(fid,'%3.2f\t',rr); % This will write text to a file 
fprintf(fid,'\n');
fprintf(fid,'%3.2f\t',rr + 2);

fclose(fid);

%% 9.9 - eval

numArrays = 10; 
A = cell(numArrays,1); 
for n = 1:numArrays 
	A{n} = magic(n); 
    Eval(['A', int2str(n), ' = magic(n)']);
End

A{5}

Eval(['A', int2str(n), ' = magic(n)']);

%% structures and cells

cell1 = {'apple', 'oranges'} % indexed by whole element no longer each item 
% to index cell 1 you would do - cell1{1} 
% number of elements no longer have to be equal 

% Structures - similar to a dictionary (nested set of varibles) 
% Can add levels - will expand for all the varibles created within the
% structure - data(2).subject - go into data structure (calling the 2nd
% value of the subject column) 
% Can vectorize them data(:).subject - will show all subjects
% Can have muiltiple levels of embedded values inside the structure 

%% Try - catch commands 
% try -- some commands, catch -- some other commands -- end 
% execute commands within the 'try' unitl it returns an error, then it will
% execute the catch commands 

