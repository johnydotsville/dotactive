// TODO: написать юнит-тест для этого класса
export class ParamsBag {
  private params: Map<string, ParamType>;


  public constructor() {
    this.params = new Map();
  }

  
  public put(param: ParamType): void {
    this.params.set(param.name, param);
  }


  public getAll(): ParamType[] {
    return Array.from(this.params.values());
  }


  public getAllGroupped(): Record<string, ParamType[]> {
    const groupsObj = Array
      .from(this.params.values())
      .reduce((acc, p) => {
          if (!acc[p.group]) {
            acc[p.group] = [];
          }
          acc[p.group].push(p);
          return acc;
        }, {});
    return groupsObj;
  }
}


export class ParamType {
  public readonly name: string;
  public readonly value: any;
  public readonly group: string;

  public constructor(name: string, value: any, group: string) { 
    this.name = name;
    this.value = value;
    this.group = group;
  }
}



/*

export class ParamsBag {
  private params: Map<string, Set<ParamType>>;


  public constructor() {
    this.params = new Map();
  }

  
  public put(param: ParamType): void {
    let params = this.params.get(param.group);
    if (!params) {
      params = new Set();
      params.add(param);
      this.params.set(param.group, params);
    } else {
      params.add(param);
    }
  }


  public getAll() {
    const arr: ParamType[] = [];
    for (let p of this.params.values()) {
      arr.push(...Array.from(p));
    }
    return arr;
  }


  public getAllGroupped() {
    
  }
}


export class ParamType {
  public readonly name: string;
  public readonly value: any;
  public readonly group: string;

  public constructor(name: string, value: any, group: string) { 
    this.name = name;
    this.value = value;
    this.group = group;
  }
}

*/