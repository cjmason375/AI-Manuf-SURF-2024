clc; close all; clear;

%% Import phase data
opts1 = delimitedTextImportOptions("NumVariables", 7);

% Specify range and delimiter
opts1.DataLines = [2, Inf];
opts1.Delimiter = ",";

% Specify column names and types
opts1.VariableNames = ["time", "time_diff", "accum_time", "phase_A", "phase_B", "phase_C", "Neutral"];
opts1.VariableTypes = ["datetime", "double", "double", "double", "double", "double", "double"];

% Specify file level properties
opts1.ExtraColumnsRule = "ignore";
opts1.EmptyLineRule = "read";

% Specify variable properties
opts1 = setvaropts(opts1, "time", "InputFormat", "yyyy-MM-dd HH:mm:ss.SSS");

% Import the phase data
data1 = readtable("APEX2_raw_processing_mergedTable.csv", opts1);
clear opts1

%% Import occurrence data
opts2 = delimitedTextImportOptions("NumVariables", 8);

% Specify range and delimiter
opts2.DataLines = [2, Inf];
opts2.Delimiter = ",";

% Specify column names and types
opts2.VariableNames = ["Status", "Time", "Adjusted_Time", "Recipes", "User", "Notes", "Adjust_Time_Value", "Graph_Value"];
opts2.VariableTypes = ["string", "datetime", "datetime", "string", "string", "string", "double", "double"];

% Specify file level properties
opts2.ExtraColumnsRule = "ignore";
opts2.EmptyLineRule = "read";

% Specify variable properties
opts2 = setvaropts(opts2, "Time", "InputFormat", "MM/dd/yyyy HH:mm:ss");

% Import the occurrence data
data2 = readtable("plasma_etch_log.csv", opts2);
clear opts2

%% Plotting phase data and vertical lines
figure(1)

% Plot phase data
plot(data1.time, data1.phase_A,'-.') % plotting PhaseA
hold on
plot(data1.time, data1.phase_B,'--') % plotting PhaseB
plot(data1.time, data1.phase_C,':') % plotting PhaseC
plot(data1.time, data1.Neutral,'-') % plotting Neutral Phase
%plot(data1.time, data1.phase_A, 'DisplayName', 'Phase_A','-') % plotting PhaseA
%plot(data1.time, data1.phase_B, 'DisplayName', 'Phase_B','--') % plotting PhaseB
%plot(data1.time, data1.phase_C, 'DisplayName', 'Phase_C',':') % plotting PhaseC
%plot(data1.time, data1.Neutral, 'DisplayName', 'Neutral','-.') % plotting Neutral phase

% Plot vertical lines from occurrence data
for i = 1:height(data2)
    x = data2.Adjusted_Time(i);
    y = data2.Graph_Value(i);
    status = data2.Status(i);
    recipe = data2.Recipes(i); % Get the recipe label
    
    % Determine the color based on status
    if strcmp(status, 'Green')
        color = 'g';
    elseif strcmp(status, 'Yellow')
        color = 'y';
    elseif strcmp(status, 'Red')
        color = 'r';
    else
        color = 'k'; % Default color if status is not matched
    end
    
    % Plot vertical line with the determined color
    plot([x x], [0 y-12], 'Color', color);
    
    % Add the recipe label
    text(x, y-12, recipe, 'VerticalAlignment', 'bottom', 'HorizontalAlignment', 'left', 'Rotation', 90);
end

%% Add legend to data
xlabel('Timestamp')
ylabel('Ampere (A)')
% legend('Location', 'northwest')
legend('Phase A', 'Phase B', 'Phase C', 'Neutral')
hold off
